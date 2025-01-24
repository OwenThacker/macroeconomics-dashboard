import streamlit as st
import pandas as pd
import os
from datetime import datetime
import base64

# Configure Streamlit page
st.set_page_config(
    page_title="Alterra | Feedback",
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

# Styling (matching the economic page)
st.markdown(f"""
    <style>
        .stApp > div {{
            transform: scale(0.67);
            transform-origin: top center;
            width: 200%;
            height: 150%;
            margin-left: -33%;
        }}

        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
        }}

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
            background-size: 100% 80%;
            background-position: center 0%;
            background-repeat: no-repeat;
        }}

        .company-title {{
            font-size: 6rem;
            font-weight: 700;
            color: #2E7D32;
            letter-spacing: -1px;
            margin-bottom: 0rem;
            z-index: 2;
            position: relative; /* Change absolute to relative to prevent overlap */
            margin-top: 0; /* Remove excessive negative margin */
            padding-top: 4rem; /* Add padding to create spacing from the background */
        }}

        .insight-card {{
            background: #FFFFFF;
            border-radius: 12px;
            padding: 0.5rem;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }}

        [data-testid="stSidebar"] .insight-card {{
            width: calc(150%); /* Full width minus padding */
            box-sizing: border-box;
            margin: 0.5rem 1rem;
            margin-left: 0.2rem;
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
        .stTextArea textarea {{
            border: 1px solid #2E7D32;
            border-radius: 8px;
        }}

        .stRadio div {{
            color: #2E7D32;
        }}

        .stButton button {{
            background-color: #2E7D32;
            color: white;
            border: none;
            border-radius: 8px;
            padding: 10px 20px;
        }}

        /* Top Left Alterra Branding */
        .top-left-brand {{
            position: absolute;
            top: 2rem;
            left: 2rem;
            z-index: 1000;
            font-size: 3rem;
            font-weight: 700;
            color: #2E7D32;
            letter-spacing: -1px;
            padding: 1rem;
            background-color: white;
            border-radius: 12px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }}

        /* Adjust main content to not overlap with brand */
        .main-content {{
            margin-top: 6rem;
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
    st.markdown("### Market Insights")
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

# Add Alterra branding at top left
st.markdown('<div class="company-title">ALTERRA</div>', unsafe_allow_html=True)

# Feedback Section
st.markdown("""
    <div style="margin-top: -2rem; margin-left: -2rem; padding: 2rem;">
        <div class="insight-card">
            <div class="insight-title">Help Us Improve</div>
            <div class="insight-content">
                We're committed to providing the most valuable economic intelligence platform. 
                Your feedback helps us understand how we can better serve your needs.
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Feedback Form
FEEDBACK_FILE = "user_feedback.csv"
if not os.path.exists(FEEDBACK_FILE):
    pd.DataFrame(columns=["Timestamp", "User Type", "Platform Value", "Additional Comments"]).to_csv(FEEDBACK_FILE, index=False)

with st.form("feedback_form"):
    st.markdown("<div class='insight-card'>", unsafe_allow_html=True)
    
    user_type = st.selectbox(
        "Who are you?", 
        ["Select your role", "Firm Owner", "Investment Manager", "Research Analyst", "Investor", "Other"]
    )
    
    platform_value = st.radio(
        "Did our platform provide valuable insights?", 
        ["Highly Valuable", "Somewhat Valuable", "Not Valuable"]
    )
    
    comments = st.text_area(
        "Any additional thoughts or suggestions?", 
        height=150, 
        placeholder="Share your feedback here..."
    )
    
    submit = st.form_submit_button("Submit Feedback")
    st.markdown("</div>", unsafe_allow_html=True)

# Handle Submission
if submit:
    if user_type == "Select your role":
        st.error("Please select your role")
    else:
        # Prepare feedback data
        feedback_data = {
            "Timestamp": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
            "User Type": [user_type],
            "Platform Value": [platform_value],
            "Additional Comments": [comments]
        }
        
        # Save to CSV
        feedback_df = pd.read_csv(FEEDBACK_FILE)
        new_entry = pd.DataFrame(feedback_data)
        feedback_df = pd.concat([feedback_df, new_entry], ignore_index=True)
        feedback_df.to_csv(FEEDBACK_FILE, index=False)
        
        st.success("Thank you for your feedback!")

# Footer
st.markdown(f"""
    <div style="background: #F8FAFC; padding: 2rem; margin-top: 3rem; text-align: center; border-top: 1px solid #E0E0E0;">
        <div style="color: #90A4AE; font-size: 0.9rem;">Powered by</div>
        <div style="color: #2E7D32; font-size: 1.2rem; font-weight: 600; margin-top: 0.5rem;">ALTERRA</div>
        <div style="color: #90A4AE; font-size: 0.8rem; margin-top: 1rem;">
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
    </div>
""", unsafe_allow_html=True)