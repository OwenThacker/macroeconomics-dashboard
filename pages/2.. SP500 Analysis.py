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
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">SP500 Analysis</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            This page presents an analysis of the S&P 500 index with respect to key economic indicators. The goal is to explore the relationships between macroeconomic data and market performance, offering insights 
            that may inform strategic investment decisions.
        </p>
    </div>
""", unsafe_allow_html=True)

# Define plot descriptions
PLOT_DESCRIPTIONS = {
    "sp500_gdp_mom.html": """
        The analysis demonstrates a strong correlation between the S&P 500 performance and U.S. GDP growth.
        Historical data reveals that movements in either often provide a directional bias for the other, 
        making GDP a useful indicator for market positioning.
    """,
    
    "sp500_cpi_mom.html": """
        The correlation between the S&P 500 and CPI shows a general upward trend, though the relationship is looser.
        This suggests that while there is some level of alignment, other factors should also be considered in analysis.
    """,
    
    "sp500_ppi_mom.html": """
        A more random and loosely correlated movement is observed here. While PPI impacts inflation trends, 
        its relationship with the S&P 500 appears inconsistent and should be interpreted with caution.
    """,
    
    "sp500_unemp_mom.html": """
        Visually, the line plots provide no significant correlation between unemployment figures and the 
        S&P 500 performance in this analysis.
        However, the momentum indicator is a good confirmation indicator.
    """,
    
    "sp500_ir_mom.html": """
        A strong correlation is evident between interest rates and S&P 500 performance, with interest rates often acting 
        as a leading indicator. This relationship can be leveraged to anticipate market movements, offering valuable 
        forward-looking insights for strategic investment planning.
    """
}

# Define the plot files, titles, and sizes
PLOT_FILES = [
    ("sp500_gdp_mom.html", "SP500 GDP MOM Analysis", 2200, 1000),
    ("sp500_cpi_mom.html", "SP500 CPI MOM Analysis", 2200, 1000),
    ("sp500_ppi_mom.html", "SP500 PPI MOM Analysis", 2200, 1000),
    ("sp500_unemp_mom.html", "SP500 Unemployment MOM Analysis", 2200, 1000),
    ("sp500_ir_mom.html", "SP500 Interest Rate MOM Analysis", 2200, 1000)
]

# Path to the plots folder
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display the plots with specified sizes
for plot_file, plot_title, width, height in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        
        st.markdown(f"### {plot_title}")
        
        # Add description with styled container
        if plot_file in PLOT_DESCRIPTIONS:
            st.markdown(f"""
                <div style='
                    padding: 15px;
                    margin-bottom: 25px;
                    background-color: #f8f9fa;
                    border-left: 4px solid #1f77b4;
                    font-size: 0.95em;
                    line-height: 1.6;
                '>
                    {PLOT_DESCRIPTIONS[plot_file]}
                </div>
            """, unsafe_allow_html=True)
        
        # Embed the plot dynamically based on width and height
        html = f'''
            <div style="
                width: {width}px;
                height: {height}px;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                overflow: hidden;
            ">
                {html_content}
            </div>
        '''
        components.html(html, height=height)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

# Overview and Implications
st.markdown("""
**Key Takeaways:**

- **Interest Rates**: Strongly correlated with the S&P 500, serving as a potential leading indicator for market performance. 
- **GDP Growth**: A significant correlation indicates that economic growth trends often mirror S&P 500 performance, providing directional bias for market positioning.
- **Inflation (CPI and PPI)**: While these metrics show some correlation, the relationship is less defined, suggesting that inflationary trends might influence long term market behavior, but not always predictably.
- **Unemployment**: Little correlation observed with market performance in the short term, but long-term trends may offer additional conirmation.

**Implications for Decision-Making:**
- Investors can leverage these relationships to better anticipate market shifts and refine their strategies. 
- Interest rates, GDP growth, and inflation trends are especially useful for identifying potential changes in market direction.
- However, caution should be exercised with metrics like unemployment, which show less immediate impact on market movements.
""")
