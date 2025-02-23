import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import os
import base64

# Configure Streamlit page
st.set_page_config(
    page_title="Alterra | Economic Overview Dashboard",
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

st.markdown(f"""
    <style>
    
        .stApp > div {{
            transform: scale(0.67);
            transform-origin: top center;
            width: 200%; /* Compensate for scaling down */
            height: 150%;
            margin-left: -33%; /* Adjust negative margin to shift content right */
        }}

        /* Sidebar Styles */
        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
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

    </style>
""", unsafe_allow_html=True)

# Sidebar Content
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <h1>ALTERRA</h1>
            <p>Economic Intelligence</p>
        </div>
    """, unsafe_allow_html=True)

    # Market Status
    current_time = datetime.now()
    market_status = "Active" if 9 <= current_time.hour <= 16 else "Closed"
    status_color = "#2E7D32" if market_status == "Active" else "#9E9E9E"

    st.markdown(f"""
        <div class="market-status">
            <div style="font-size: 0.9rem; color: #90A4AE;">MARKET STATUS</div>
            <div style="font-size: 1.1rem; color: {status_color}; font-weight: 500;">
                ● {market_status}
            </div>
            <div style="font-size: 0.8rem; color: #90A4AE; margin-top: 0.5rem;">
                {current_time.strftime('%H:%M:%S UTC')}
            </div>
        </div>
    """, unsafe_allow_html=True)

    ## Market Insights
    st.markdown("### Top New Market Insights", unsafe_allow_html=True)
    insights = [
        {
            "title": "Global Tech Sell Off",
            "content": "Investor concern with the new release of China's DeepSeek model. Nvidia falls 14% in premarket trading",
            "trend": "↘️ Falling",  # Changed to diagonal downward arrow
            "impact": "High"
        },
        {
            "title": "Fed Holding Rates",
            "content": "Fed rate cut 'probably not until the second half of the year' says economist Odeta Kushi of First American",
            "trend": "→ Stable",
            "impact": "High"
        },
        {
            "title": "Highest interest rates in Japan in 17 Years",
            "content": "BoJ raises short-term policy rate 25 bps to 0.5% from 0.25%, causing a jump in the Yen",
            "trend": "↗️ Growing",
            "impact": "High"
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

# Main Content Area
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">
            USA Economic Health Dashboard
        </h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            Comprehensive analysis of key economic indicators through interactive visualizations,
            providing insights into fiscal health and economic stability
        </p>
    </div>
""", unsafe_allow_html=True)

# Quick Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("GDP Growth", "2.4%", "0.2%")
with col2:
    st.metric("Inflation Rate", "3.1%", "-0.5%")
with col3:
    st.metric("Unemployment", "3.8%", "-0.1%")
with col4:
    st.metric("Interest Rate", "5.25%", "0%")

# Main Content Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Fiscal Health", "Economic Indicators", "Analysis"])

with tab1:
    st.markdown("### Economic Overview")
    view_type = st.selectbox("View Type", ["Standard", "Detailed", "Compact"], key="overview_view")
    
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
            # Embed plots dynamically
            components.html(
                html_content,  # Use the raw HTML content
                width=2400,  # Set the iframe width to 2400px
                height=650,  # Adjust height as needed or leave it as is
                scrolling=True  # Enable scrolling for content overflow
            )


            st.markdown('</div>', unsafe_allow_html=True)

        else:
            st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

with tab2:
    # Fiscal Health Tab
    st.markdown("### Fiscal Health Metrics")
    metric_type = st.selectbox("Metric Type", ["All", "Debt", "Revenue", "Expenditure"], key="fiscal_metric")
    
    # Display relevant plots based on metric type
    if metric_type in ["All", "Debt"]:
        if os.path.exists(os.path.join(PLOTS_PATH, "Interest_Cov_Ratio.html")):
            st.markdown("#### Interest Coverage Ratio")
            components.html(
                open(os.path.join(PLOTS_PATH, "Interest_Cov_Ratio.html")).read(),
                height=650,
                width=2400
            )
    
    if metric_type in ["All", "Revenue"]:
        if os.path.exists(os.path.join(PLOTS_PATH, "usa_sur_def.html")):
            st.markdown("#### Surplus/Deficit")
            components.html(
                open(os.path.join(PLOTS_PATH, "usa_sur_def.html")).read(),
                height=650,
                width=2400
            )

with tab3:
    # Economic Indicators Tab
    st.markdown("### Economic Indicators")
    
    # Add indicator filters
    indicator_type = st.multiselect(
        "Select Indicators",
        ["GDP", "Inflation", "Employment", "Trade Balance", "Industrial Production"],
        default=["GDP", "Inflation"]
    )
    
    st.info("Select indicators to display relevant charts")

with tab4:
    # Analysis Tab
    st.markdown("### Economic Analysis")
    
    # Add analysis tools
    analysis_type = st.selectbox(
        "Analysis Type",
        ["Trend Analysis", "Correlation Analysis", "Forecast", "Risk Assessment"]
    )
    
    # Add export options
    col1, col2, col3 = st.columns([2,2,1])
    with col3:
        st.download_button("Export Analysis", "Analysis data", "analysis.csv")

# Footer
st.markdown("""
---
<div style="text-align: center; padding: 1rem;">
    <p style="color: #666666;">Data updated as of {}</p>
    <p style="color: #666666; font-size: 0.8rem;">
        Sources: Federal Reserve Economic Data (FRED), Bureau of Labor Statistics (BLS), 
        Bureau of Economic Analysis (BEA)
    </p>
</div>
""".format(current_time.strftime('%Y-%m-%d %H:%M UTC')), unsafe_allow_html=True)
