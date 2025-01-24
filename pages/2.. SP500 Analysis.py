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

        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
        }}

        .hero-container {{
            position: relative;
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

# Main Content
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">S&P 500 Analysis</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 2400px;">
            Explore interactive visualizations of economic trends and asset behavior across various market conditions.
        </p>
    </div>
""", unsafe_allow_html=True)

# Quick Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="S&P 500", value="6,049.24", delta="1,198.81 (24.72%) Past Year")
with col2:
    st.metric(label="GDP Growth", value="2.5%", delta="0.3%")
with col3:
    st.metric(label="Inflation Rate", value="3.4%", delta="-0.1%")
with col4:
    st.metric(label="Unemployment", value="3.7%", delta="0.0%")

# Main Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Economic Indicators", "Market Analysis", "Reports"])

with tab1:
    # Filters Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        time_period = st.selectbox("Time Period", 
            ["1M", "3M", "6M", "1Y", "5Y", "MAX"])
    with col2:
        chart_type = st.selectbox("Chart Type",
            ["Line", "Candlestick", "Area", "Bar"])
    with col3:
        indicators = st.multiselect("Technical Indicators",
            ["MA", "RSI", "MACD", "BB"])
    with col4:
        st.selectbox("Export Options",
            ["PDF", "CSV", "Excel", "PNG"])

    # Plot Categories
    plot_category = st.selectbox(
        "Select Analysis Category",
        ["GDP Analysis", "Inflation Metrics", "Employment Data", "Interest Rates"]
    )

    # Define plot descriptions
    PLOT_DESCRIPTIONS = {
        "sp500_gdp_mom.html": "Strong correlation between S&P 500 performance and U.S. GDP growth.",
        "sp500_cpi_mom.html": "Correlation between S&P 500 and CPI shows upward trend.",
        "sp500_ppi_mom.html": "Looser correlation observed between PPI and S&P 500.",
        "sp500_unemp_mom.html": "Limited correlation between unemployment and S&P 500.",
        "sp500_ir_mom.html": "Strong correlation between interest rates and S&P 500 performance."
    }

    # Plot files mapping
    plot_files = {
        "GDP Analysis": ["sp500_gdp_mom.html"],
        "Inflation Metrics": ["sp500_cpi_mom.html", "sp500_ppi_mom.html"],
        "Employment Data": ["sp500_unemp_mom.html"],
        "Interest Rates": ["sp500_ir_mom.html"]
    }

    # Display selected plots
    for plot_file in plot_files.get(plot_category, []):
        plot_path = os.path.join(os.path.dirname(__file__), "..", "plots", plot_file)
        if os.path.exists(plot_path):
            with open(plot_path, "rb") as f:
                html_content = f.read().decode(errors="ignore")
            
            st.markdown(f"### {plot_file.replace('.html', '').replace('_', ' ').title()}")
            if plot_file in PLOT_DESCRIPTIONS:
                st.info(PLOT_DESCRIPTIONS[plot_file])
            components.html(html_content, height=800, width=2400)

with tab2:
    st.markdown("### Economic Indicators Analysis")
    st.info("Economic indicators analysis content will be displayed here")

with tab3:
    st.markdown("### Market Analysis")
    st.info("Market analysis content will be displayed here")

with tab4:
    st.markdown("### Reports")
    st.info("Reports and documentation will be displayed here")

# Data Table Section
st.markdown("### Historical Data")
show_data = st.checkbox("Show Raw Data")
if show_data:
    st.dataframe({
        "Date": ["2024-01-22", "2024-01-21", "2024-01-20"],
        "S&P 500": [4927.23, 4911.95, 4898.67],
        "GDP": [2.5, 2.5, 2.4],
        "CPI": [3.4, 3.4, 3.5]
    })

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