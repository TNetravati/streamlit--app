import streamlit as st
import random

# Custom CSS for background and styling
def set_background():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #4a6fa5;
            background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        }
        .header {
            background-color: #4a6fa5;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }
        .course-card {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .progress-bar {
            height: 20px;
            background-color: #e0e0e0;
            border-radius: 10px;
            margin: 10px 0;
        }
        .progress-fill {
            height: 100%;
            border-radius: 10px;
            background: linear-gradient(90deg, #4facfe 0%, #00f2fe 100%);
            text-align: center;
            color: white;
            line-height: 20px;
            font-size: 12px;
        }
        .section {
            background-color: white;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        }
        </style>
        """,
        unsafe_allow_html=True
    )

set_background()

# Course Data
course_details = {
    "Python Basics": "Learn Python fundamentals, syntax, and data types.",
    "Data Science": "Explore data analysis, visualization, and statistics.",
    "Web Development": "Build websites using HTML, CSS, and JavaScript.",
    "Machine Learning": "Understand ML algorithms and build models."
}

# Session State Init
if 'enrollments' not in st.session_state:
    st.session_state.enrollments = {course: 0 for course in course_details}
if 'my_courses' not in st.session_state:
    st.session_state.my_courses = []
if 'completed_courses' not in st.session_state:
    st.session_state.completed_courses = []

# App Header
st.set_page_config(page_title="Online Education", layout="centered")
st.markdown(
    """
    <div class="header">
        <h1 style='text-align: center; color: white;'>Online Education System</h1>
        <p style='text-align: center; color: white;'>Learn at your own pace. Anytime. Anywhere.</p>
    </div>
    """, 
    unsafe_allow_html=True
)

# User Info
with st.container():
    st.subheader(" Learner Details")
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Your Name")
    with col2:
        email = st.text_input("Email Address")
    st.divider()

# Course Selection
with st.container():
    st.subheader("Choose a Course")
    selected_course = st.selectbox("Available Courses", list(course_details.keys()))
    st.markdown(
        f"""
        <div class="course-card">
            <h3>{selected_course}</h3>
            <p>{course_details[selected_course]}</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Enroll
    if st.button(" Enroll Now", type="primary"):
        if not name or not email:
            st.warning("Please enter both your name and email.")
        elif selected_course not in st.session_state.my_courses:
            st.session_state.my_courses.append(selected_course)
            st.session_state.enrollments[selected_course] += 1
            st.success(f"{name}, you have successfully enrolled in **{selected_course}**!")
        else:
            st.info("You're already enrolled in this course.")
    st.divider()

# My Courses
if st.session_state.my_courses:
    with st.container():
        st.subheader(" My Learning Dashboard")
        for course in st.session_state.my_courses:
            progress = random.randint(60, 100)
            st.markdown(
                f"""
                <div class="course-card">
                    <h4>{course}</h4>
                    <div class="progress-bar">
                        <div class="progress-fill" style="width: {progress}%">{progress}%</div>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )
            if progress >= 90 and course not in st.session_state.completed_courses:
                st.session_state.completed_courses.append(course)
        st.divider()

# Certificates
if st.session_state.completed_courses:
    with st.container():
        st.subheader(" My Certificates")
        for course in st.session_state.completed_courses:
            st.markdown(
                f"""
                <div class="section">
                    <h4>🎉 Congratulations {name}!</h4>
                    <p>You completed <strong>{course}</strong></p>
                    <pre style='background-color: #f8f9fa; padding: 10px; border-radius: 5px;'>
Certificate of Completion
Name: {name}
Course: {course}
Status: Completed
Date: {random.randint(1, 30)}/{random.randint(1, 12)}/2023
                    </pre>
                </div>
                """,
                unsafe_allow_html=True
            )
        st.divider()

# Enrollment Stats
with st.container():
    st.subheader(" Course Enrollment Stats")
    for course, count in st.session_state.enrollments.items():
        bar_width = min(count * 20, 200)
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; margin-bottom: 10px;">
                <div style="width: 150px;"><strong>{course}</strong></div>
                <div style="width: 200px; height: 20px; background-color: #e0e0e0; border-radius: 10px;">
                    <div style="width: {bar_width}px; height: 100%; border-radius: 10px; background: linear-gradient(90deg, #a1c4fd 0%, #c2e9fb 100%);"></div>
                </div>
                <div style="width: 80px; text-align: right;">{count} enrolled</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    st.divider()

# Feedback
with st.container():
    st.subheader(" Feedback")
    feedback = st.text_area("How was your learning experience?", height=100)
    if st.button("Submit Feedback"):
        if feedback.strip():
            st.success("Thank you for your feedback!")
        else:
            st.warning("Feedback cannot be empty.")
    st.divider()

# FAQs
with st.container():
    st.subheader("Frequently Asked Questions")
    with st.expander("What happens after I enroll?"):
        st.write("You'll see your progress and complete the course at your own pace.")
    with st.expander("Do I get a certificate?"):
        st.write("Yes! Once your course progress reaches 90%, you receive a certificate.")
    with st.expander("Is this platform free?"):
        st.write("Yes! All courses here are completely free.")
    st.divider()

# Contact
with st.container():
    st.subheader(" Contact Us")
    contact_msg = st.text_input("Write your message or query", key="contact_input")
    if st.button("Send Message", key="contact_button"):
        if contact_msg.strip():
            st.success("Message received! We'll respond shortly.")
        else:
            st.warning("Please enter a message.")