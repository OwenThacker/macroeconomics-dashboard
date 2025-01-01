import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="User Feedback", layout="wide")

# CSS Styling with Tightened Padding and Margins
st.markdown("""
<style>
    /* Page title styling */
    h1 {
        color: #8BC34A;
        font-size: 2.0em;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* Section Title Styling */
    .section-title { 
        font-size: 3.2em;
        font-weight: bold;
        margin: 20px 0 10px 0;
        color: #8BC34A;
        padding-left: 5px;
        border-left: 6px solid #8BC34A;
    }
    
    /* Question Text Styling */
    .question-text {
        font-size: 2.0em;
        font-weight: 600;
        color: #000000;
        margin: 5px 0 5px 0;
    }
    
    /* Radio Button Styling */
    .stRadio > div {
        font-size: 1.8em !important;
        margin: 5px 0 5px 15px !important;
    }
    
    .stRadio label {
        font-size: 2.0em !important;
    }
    
    /* Text Area Styling */
    .stTextArea textarea {
        font-size: 1.8em !important;
        border: 2px solid #e0e0e0 !important;
        border-radius: 6px !important;
        padding: 10px !important;
        background-color: #fafafa !important;
        margin: 5px 0 5px 0 !important;
    }

    .stTextArea textarea:focus {
        border-color: #8BC34A !important;
        box-shadow: 0 2px 6px rgba(139,195,74,0.3) !important;
    }
    
    /* Submit Button Styling */
    .stButton button {
        font-size: 1.8em !important;
        padding: 12px 24px !important;
        border-radius: 6px !important;
        margin-top: 15px !important;
    }
    
    .block-container {
        max-width: 1400px;
        padding-top: 1.5rem;
    }

    /* Reduce default spacing between Streamlit elements */
    .stMarkdown, .stRadio, .stTextArea {
        margin-bottom: 5px !important;
    }

    hr {
        margin: 25px 0 !important;
        border-top: 1.5px solid #e0e0e0;
    }
</style>
""", unsafe_allow_html=True)

# Initialize feedback storage
FEEDBACK_FILE = "feedback_data.csv"
if not os.path.exists(FEEDBACK_FILE):
    pd.DataFrame(columns=["User Profile", "Question", "Response"]).to_csv(FEEDBACK_FILE, index=False)

# Title
st.title("We value your feedback")

# Define Sections and Questions
sections = {
    "About You": [
        ("Which best describes you?", ["Firm Owner", "Investment Manager", "Research Analyst", "Investor", "Other"]),
        ("Please briefly describe your role and objectives when using such a platform.", "text_area")
    ],
    "Platform Potential": [
        ("What would make a platform like this indispensable to your work?", "text_area"),
        ("What specific data or insights would you expect from a platform like this?", "text_area"),
        ("How frequently would you use a platform providing detailed macroeconomic insights?", ["Daily", "Weekly", "Monthly", "Rarely"])
    ],
    "Desired Features": [
        ("What key features would you like to see implemented in the future?", "text_area"),
        ("Which asset classes or economic indicators are most important to you?", ["Equities", "Bonds", "Commodities", "Currencies", "Real Estate", "Other"])
    ],
    "Value Proposition": [
        ("What would make you consider subscribing to this platform?", "text_area"),
        ("Would tailored insights/reports for your specific needs be valuable to you?", ["Yes", "No", "Maybe"])
    ]
}

# Feedback Form
with st.form("feedback_form"):
    responses = {}

    for section, questions in sections.items():
        st.markdown(f"<div class='section-title'>{section}</div>", unsafe_allow_html=True)

        for question, answer_type in questions:
            st.markdown(f"<div class='question-text'>{question}</div>", unsafe_allow_html=True)
            if answer_type == "text_area":
                responses[question] = st.text_area("", height=100, key=question)
            else:
                responses[question] = st.radio("", answer_type, key=question)
            st.write("")

        st.markdown("<hr>", unsafe_allow_html=True)

    submit = st.form_submit_button("Submit Feedback")

# Handle Submissions
if submit:
    feedback_entries = []
    user_profile = responses.get("Which best describes you?", "N/A")
    role_description = responses.get("Please briefly describe your role and objectives when using such a platform.", "N/A")
    
    for question, response in responses.items():
        feedback_entries.append({"User Profile": user_profile, "Question": question, "Response": response})
    
    # Save responses to CSV
    feedback_df = pd.read_csv(FEEDBACK_FILE)
    new_feedback = pd.DataFrame(feedback_entries)
    feedback_df = pd.concat([feedback_df, new_feedback], ignore_index=True)
    feedback_df.to_csv(FEEDBACK_FILE, index=False)
    
    st.success("Thank you for your feedback! Your responses have been recorded.")

# Download Feedback Data
st.markdown("### Download Feedback Data")
with open(FEEDBACK_FILE, "rb") as file:
    st.download_button(
        label="Download Feedback CSV",
        data=file,
        file_name="feedback_data.csv",
        mime="text/csv"
    )
