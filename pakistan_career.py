import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

# --------------------------
# CONFIG
# --------------------------
st.set_page_config(page_title="Career Counseling Pro", layout="wide")

# --------------------------
# SESSION LOGIN
# --------------------------
if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# --------------------------
# HEADER
# --------------------------
col1, col2 = st.columns([1,4])
with col1:
    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135755.png", width=120)
with col2:
    st.markdown("<h1 style='color:#1F618D;'>Pakistan Career Counseling System</h1>", unsafe_allow_html=True)
    st.markdown("<h4 style='color:gray;'>AI-Based Academic & Personality Guidance Platform</h4>", unsafe_allow_html=True)

st.divider()

menu = st.sidebar.selectbox("Navigation", ["Student Counseling", "Admin Login"])

# ========================================
# STUDENT SECTION
# ========================================
if menu == "Student Counseling":

    name = st.text_input("Enter Student Name")

    if name:

        streams = {
            "Pre-Medical": 0,
            "Pre-Engineering": 0,
            "ICS": 0,
            "ICom": 0
        }

        # MBTI Scores
        mbti = {"I":0,"E":0,"T":0,"F":0,"S":0,"N":0,"J":0,"P":0}

        st.subheader("Academic Interest Questions")

        q1 = st.radio("Favourite Subject?", ["Biology","Math","Computer","Accounting"])
        q2 = st.radio("Preferred Career Type?", ["Doctor","Engineer","Software Developer","Businessman"])

        # Stream Scoring
        if q1 == "Biology": streams["Pre-Medical"] += 2
        if q1 == "Math": streams["Pre-Engineering"] += 2
        if q1 == "Computer": streams["ICS"] += 2
        if q1 == "Accounting": streams["ICom"] += 2

        if q2 == "Doctor": streams["Pre-Medical"] += 2
        if q2 == "Engineer": streams["Pre-Engineering"] += 2
        if q2 == "Software Developer": streams["ICS"] += 2
        if q2 == "Businessman": streams["ICom"] += 2

        st.subheader("Personality (MBTI) Questions")

        p1 = st.radio("You prefer:", ["Working Alone","Working in Teams"])
        p2 = st.radio("You decide based on:", ["Logic","Emotions"])
        p3 = st.radio("You focus more on:", ["Practical Facts","Future Possibilities"])
        p4 = st.radio("You are more:", ["Organized","Flexible"])

        # MBTI Scoring
        if p1 == "Working Alone": mbti["I"] += 1
        else: mbti["E"] += 1

        if p2 == "Logic": mbti["T"] += 1
        else: mbti["F"] += 1

        if p3 == "Practical Facts": mbti["S"] += 1
        else: mbti["N"] += 1

        if p4 == "Organized": mbti["J"] += 1
        else: mbti["P"] += 1

        if st.button("Generate Full Report"):

            recommended_stream = max(streams, key=streams.get)

            personality = ""
            personality += "I" if mbti["I"] >= mbti["E"] else "E"
            personality += "T" if mbti["T"] >= mbti["F"] else "F"
            personality += "S" if mbti["S"] >= mbti["N"] else "N"
            personality += "J" if mbti["J"] >= mbti["P"] else "P"

            st.success(f"🎓 Recommended Stream: {recommended_stream}")
            st.info(f"🧠 Personality Type: {personality}")

            # Save Data
            data = pd.DataFrame([[name, recommended_stream, personality]],
                                columns=["Name","Stream","Personality"])

            if os.path.exists("student_data.csv"):
                data.to_csv("student_data.csv", mode='a', header=False, index=False)
            else:
                data.to_csv("student_data.csv", index=False)

            # Radar Chart
            st.subheader("🧠 Personality Radar Chart")

            categories = list(mbti.keys())
            values = list(mbti.values())

            angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
            values += values[:1]
            angles += angles[:1]

            fig = plt.figure()
            ax = fig.add_subplot(111, polar=True)
            ax.plot(angles, values)
            ax.fill(angles, values, alpha=0.25)
            ax.set_xticks(angles[:-1])
            ax.set_xticklabels(categories)

            st.pyplot(fig)

# ========================================
# ADMIN LOGIN
# ========================================
elif menu == "Admin Login":

    password = st.text_input("Enter Admin Password", type="password")

    if st.button("Login"):
        if password == "admin123":
            st.session_state.admin_logged_in = True
            st.success("Admin Logged In Successfully")
        else:
            st.error("Incorrect Password")

    if st.session_state.admin_logged_in:

        st.subheader("📊 Admin Dashboard")

        if os.path.exists("student_data.csv"):
            df = pd.read_csv("student_data.csv")

            st.write("Total Students:", len(df))
            st.dataframe(df)

            fig2, ax2 = plt.subplots()
            df["Stream"].value_counts().plot(kind='bar', ax=ax2)
            st.pyplot(fig2)

        else:
            st.warning("No student data available.")