import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="Economic Health Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get the absolute path to the image file
image_path = os.path.join(os.getcwd(), 'plots', 'sp500_gdp.png')

# Function to encode image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

# Get the base64 encoded image
image_base64 = image_to_base64(image_path)

# Reuse the same CSS styles from the economic page with additional homepage-specific styles
st.markdown(f"""
    <style>
        /* Sidebar Styles */
        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
            width: 250px;  /* Adjusted width */
        }}
        
        .main {{
            background-color: #FFFFFF;
        }}
        
        /* Hero Section Styles */
        .hero-container {{
            position: relative;
            padding: 6rem 2rem;
            text-align: center;
            margin: -4rem -4rem 1rem -4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            background-image: url("{image_base64}");
            background-size: 100% 80%; /* Adjust the size of the image vertically */
            background-position: center 0%; /* Move the image down */
            background-repeat: no-repeat;
        }}

        /* Hero Title Styles */
        .company-title {{
            font-size: 6rem;
            font-weight: 700;
            color: #2E7D32; /* Dark green title */
            letter-spacing: -1px;
            margin-bottom: 1rem;
            z-index: 2; /* Ensure the title is above the image */
            margin-top: -40rem;
        }}
        
        .company-subtitle {{
            font-size: 2rem;
            color: #2E7D32;
            max-width: 800px;
            margin: 0 auto;
            z-index: 2;
        }}
        
        /* Market Insight Cards (Market Pulse Cards) */
        .insight-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            padding: 2rem 0;
            margin-top: -25rem;
        }}
        
        .insight-card {{
            background: #FFFFFF;
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }}
        
        .insight-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }}
        
        .insight-title {{
            font-size: 1.2rem;
            color: #2E7D32;
            font-weight: 600;
        }}
        
        .insight-content {{
            font-size: 1.0rem;
            color: #262626;
            margin-top: 0.5rem;
        }}
        
        .insight-footer {{
            font-size: 0.9rem;
            color: #90A4AE;
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }}
        
        .insight-impact {{
            color: #2E7D32;
            font-weight: 600;
        }}

        /* Market Insights header */
        .market-insights-header {{
            margin-bottom: 0.5rem;
            margin-top: -25rem;
        }}

        /* About Section */
        .about-section {{
            background: #F8F9FA;
            border-radius: 16px;
            padding: 4rem 2rem;
            margin: 2rem 0;
        }}
        
        .feature-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }}
        
        .feature-card {{
            background: #FFFFFF;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
        }}
        
        .feature-card:hover {{
            border-color: #2E7D32;
        }}
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
            width: 250px;  /* Sidebar width adjustment */
        }}

        .stSidebar h1 {{
            font-size: 1.8rem;
            font-weight: 600;
            color: #2E7D32;
            text-align: center;
        }}

        .stSidebar p {{
            color: #90A4AE;
            margin-top: 0.5rem;
            text-align: center;
        }}

        /* Dropdown Styling */
        .stSelectbox div[data-baseweb="select"] {{
            border: none;  /* Remove the border */
            border-radius: 8px;
            padding: 0.4rem;  /* Adjust padding for better fit */
            font-size: 1rem;  /* Make text clearer */
            color: #2E7D32;   /* Green text color */
            background-color: #FFFFFF; /* Ensure white background */
        }}

        .stSelectbox div[data-baseweb="select"]:focus-within {{
            outline: none;  /* Remove the default blue outline */
            box-shadow: 0 0 0 2px rgba(46, 125, 50, 0.5);  /* Green shadow on focus */
        }}

        .stSelectbox div[data-baseweb="select"] > div {{
            border: none !important;  /* Remove any border around dropdown */
        }}

        .stSelectbox label {{
            margin-bottom: 0.2rem !important;  /* Reduce gap around label */
        }}
    </style>
""", unsafe_allow_html=True)

# Sidebar Configuration
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h1 style="color: #2E7D32; font-size: 1.8rem; font-weight: 600;">ALTERRA</h1>
            <p style="color: #90A4AE; margin-top: 0.5rem;">Economic Intelligence</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Market Status Indicator
    current_time = datetime.now()
    market_status = "Active" if 9 <= current_time.hour <= 16 else "Closed"
    status_color = "#2E7D32" if market_status == "Active" else "#9E9E9E"
    
    st.markdown(f"""
        <div style="background: #F8F9FA; padding: 1rem; border-radius: 8px; margin: 1rem 0;">
            <div style="font-size: 0.9rem; color: #90A4AE;">MARKET STATUS</div>
            <div style="font-size: 1.1rem; color: {status_color}; font-weight: 500;">
                ● {market_status}
            </div>
            <div style="font-size: 0.8rem; color: #90A4AE; margin-top: 0.5rem;">
                {current_time.strftime('%H:%M:%S UTC')}
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    # Market Insights
    st.markdown("### Market Insights", unsafe_allow_html=True)
    insights = [
        {
            "title": "Energy Impact Alert",
            "content": "Energy prices surge 15% - logistics sector under pressure",
            "trend": "↗️ Rising",
            "impact": "High"
        },
        {
            "title": "Supply Chain Update",
            "content": "Regional commerce shows 20% growth in Q1",
            "trend": "↗️ Growing",
            "impact": "Medium"
        },
        {
            "title": "Tech Sector Analysis",
            "content": "Enterprise solutions maintain 12% growth rate",
            "trend": "→ Stable",
            "impact": "Moderate"
        }
    ]
    
    for insight in insights:
        st.markdown(f"""
            <div class="insight-card">
                <div class="insight-title">{insight['title']}</div>
                <div class="insight-content">{insight['content']}</div>
                <div class="insight-footer">
                    <div>{insight['trend']}</div>
                    <div class="insight-impact">{insight['impact']}</div>
                </div>
            </div>
        """, unsafe_allow_html=True)


# Main Content Header
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">Feedback</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            We value your feedback.
        </p>
    </div>
""", unsafe_allow_html=True)

# Initialize feedback storage
FEEDBACK_FILE = "feedback_data.csv"
if not os.path.exists(FEEDBACK_FILE):
    pd.DataFrame(columns=["User Profile", "Question", "Response"]).to_csv(FEEDBACK_FILE, index=False)

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
                responses[question] = st.text_area(question, height=100, key=question)
            else:
                responses[question] = st.radio(question, answer_type, key=question)
            st.write("")  # Adds a small space between questions

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
