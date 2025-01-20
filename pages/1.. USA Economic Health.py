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
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">USA Economic Health Dashboard</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            Comprehensive analysis of key economic indicators through interactive visualizations,
            providing insights into fiscal health and economic stability
        </p>
    </div>
""", unsafe_allow_html=True)

# Plot descriptions
PLOT_DESCRIPTIONS = {
    "DGDP_Ratio.html": "The Debt-to-GDP ratio shows a manageable upward trajectory, indicating controlled debt management and fiscal stability.",
    "usa_revenue.html": "Revenue trends demonstrate steady Month-over-Month growth, supporting fiscal health and stability.",
    "Interest_Cov_Ratio.html": "Improvement in Interest Coverage Ratio indicates efficient debt management and stronger fiscal health.",
    "usa_sur_def.html": "Improvement in the surplus/deficit position highlights effective fiscal management and financial stability."
}

# Plot details
PLOT_FILES = [
    ("DGDP_Ratio.html", "Debt-to-GDP Ratio", "100%", 650),
    ("usa_revenue.html", "USA Revenue", "100%", 650),
    ("Interest_Cov_Ratio.html", "Interest Coverage Ratio", "100%", 650),
    ("usa_sur_def.html", "USA Surplus/Deficit", "100%", 650)
]

PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display plots with descriptions
for plot_file, plot_title, max_width, max_height in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        st.markdown(f"### {plot_title}")
        
        # Add description
        if plot_file in PLOT_DESCRIPTIONS:
            st.markdown(f"""
                <div class="description-box">
                    {PLOT_DESCRIPTIONS[plot_file]}
                </div>
            """, unsafe_allow_html=True)
        
        # Plot container
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        html_base64 = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
        st.components.v1.html(
            f"""
            <iframe src="data:text/html;base64,{html_base64}" 
                    width="{max_width}" height="{max_height}"></iframe>
            """, 
            height=max_height
        )
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

# Key Takeaways Section
st.markdown("""
    <div class="takeaways-container">
        <h3>Key Takeaways</h3>
        
        <div class="takeaway-item">
            <strong>Economic Health Score</strong><br>
            The current economic health score suggests a robust and stable economy with sustained growth momentum. 
            Continuous monitoring remains crucial in the dynamic global economic landscape.
        </div>
        
        <div class="takeaway-item">
            <strong>Debt-to-GDP Ratio</strong><br>
            While rising, the ratio remains at manageable levels, suggesting controlled fiscal policy. 
            Monitoring is essential as significant increases could signal potential risks.
        </div>
        
        <div class="takeaway-item">
            <strong>Revenue Trends</strong><br>
            Consistent growth indicates healthy economic activity and strong fiscal management, 
            supporting essential policies without significant debt accumulation.
        </div>
        
        <div class="takeaway-item">
            <strong>Interest Coverage Ratio</strong><br>
            Favorable trends signal effective debt obligation management, 
            reducing fiscal strain risks.
        </div>
        
        <div class="takeaway-item">
            <strong>Surplus/Deficit Position</strong><br>
            Improving position reflects effective fiscal management and balanced expenditures, 
            providing flexibility for future economic policy maneuvers.
        </div>
        
        <h3>Implications for Decision-Making</h3>
        
        <div class="takeaway-item">
            <strong>Policy-makers</strong><br>
            Current stability supports long-term investments and infrastructure development, 
            though caution is needed regarding global uncertainties.
        </div>
        
        <div class="takeaway-item">
            <strong>Investors</strong><br>
            Positive revenue trends and manageable debt levels present a favorable investment environment, 
            while maintaining awareness of potential risks.
        </div>
        
        <div class="takeaway-item">
            <strong>General Outlook</strong><br>
            Strong, sustainable fiscal environment with emphasis on monitoring debt levels and global risks. 
            Data should inform long-term financial strategies for both government and private sector planning.
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style="background: #F8FAF8; padding: 2rem; margin-top: 3rem; text-align: center; border-top: 1px solid #E0E7E0;">
        <div style="color: #4A634A; font-size: 0.9rem;">Last updated: {}</div>
    </div>
""".format(datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')), unsafe_allow_html=True)
