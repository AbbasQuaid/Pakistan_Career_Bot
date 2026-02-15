import streamlit as st
import matplotlib.pyplot as plt

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Pakistan Career Counseling Bot",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Pakistan Career Counseling ChatBot")
st.write("Helping Students Choose the Right Academic Stream")

st.divider()

# ----------------------------
# User Input
# ----------------------------
name = st.text_input("Enter your Name:")

if name:

    st.subheader("Answer the Following Questions")

    # Initialize scores
    scores = {
        "FSc Pre-Medical": 0,
        "FSc Pre-Engineering": 0,
        "ICS (Computer Science)": 0,
        "ICom (Commerce)": 0
    }

    # ----------------------------
    # Questions
    # ----------------------------

    q1 = st.radio(
        "1️⃣ Which subject do you enjoy the most?",
        ["Biology", "Mathematics", "Computer Science", "Accounting"]
    )

    q2 = st.radio(
        "2️⃣ What type of work excites you?",
        ["Treating Patients",
         "Designing Machines",
         "Programming & AI",
         "Managing Business"]
    )

    q3 = st.radio(
        "3️⃣ What kind of environment do you prefer?",
        ["Hospital / Lab",
         "Engineering Site",
         "Office / Software House",
         "Bank / Corporate Office"]
    )

    # ----------------------------
    # Recommendation Button
    # ----------------------------

    if st.button("Get Career Recommendation"):

        # Question 1 Scoring
        if q1 == "Biology":
            scores["FSc Pre-Medical"] += 3
        elif q1 == "Mathematics":
            scores["FSc Pre-Engineering"] += 3
        elif q1 == "Computer Science":
            scores["ICS (Computer Science)"] += 3
        elif q1 == "Accounting":
            scores["ICom (Commerce)"] += 3

        # Question 2 Scoring
        if q2 == "Treating Patients":
            scores["FSc Pre-Medical"] += 3
        elif q2 == "Designing Machines":
            scores["FSc Pre-Engineering"] += 3
        elif q2 == "Programming & AI":
            scores["ICS (Computer Science)"] += 3
        elif q2 == "Managing Business":
            scores["ICom (Commerce)"] += 3

        # Question 3 Scoring
        if q3 == "Hospital / Lab":
            scores["FSc Pre-Medical"] += 2
        elif q3 == "Engineering Site":
            scores["FSc Pre-Engineering"] += 2
        elif q3 == "Office / Software House":
            scores["ICS (Computer Science)"] += 2
        elif q3 == "Bank / Corporate Office":
            scores["ICom (Commerce)"] += 2

        # ----------------------------
        # Final Result
        # ----------------------------

        recommended_stream = max(scores, key=scores.get)

        st.success(f"🎯 {name}, Your Recommended Stream is: {recommended_stream}")

        st.subheader("Suggested Career Options")

        if recommended_stream == "FSc Pre-Medical":
            st.write("• MBBS")
            st.write("• BDS")
            st.write("• DPT")
            st.write("• Pharmacy")

        elif recommended_stream == "FSc Pre-Engineering":
            st.write("• Mechanical Engineering")
            st.write("• Civil Engineering")
            st.write("• Electrical Engineering")
            st.write("• Mechatronics")

        elif recommended_stream == "ICS (Computer Science)":
            st.write("• Software Engineering")
            st.write("• AI Engineer")
            st.write("• Data Scientist")
            st.write("• Cyber Security Expert")

        elif recommended_stream == "ICom (Commerce)":
            st.write("• CA")
            st.write("• ACCA")
            st.write("• Banking")
            st.write("• Business Management")

        # ----------------------------
        # Chart Visualization
        # ----------------------------

        st.subheader("📊 Interest Score Comparison")

        streams = list(scores.keys())
        values = list(scores.values())

        fig, ax = plt.subplots()
        ax.bar(streams, values)
        plt.xticks(rotation=20)
        plt.ylabel("Score")
        plt.title("Career Stream Score Comparison")

        st.pyplot(fig)

        st.info("Note: This recommendation is based on your interests only.")