import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import os
import base64

# Configure Streamlit page
st.set_page_config(
    page_title="Alterra | Bond Market Dashboard",
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

# Define plot configurations
PLOT_CONFIG = {
    "Yield_Curve_with_Steepness.html": {
        "height": 1000,
        "category": "Yield Analysis",
        "description": "Current yield curve shape with steepness indicator."
    },
    "CIR_Model.html": {
        "height": 400,
        "category": "Rate Forecasts",
        "description": "Cox-Ingersoll-Ross model predictions for rate behavior."
    },
    "CIR_Model_MonteCarlo_Hist.html": {
        "height": 400,
        "category": "Rate Forecasts",
        "description": "Monte Carlo simulations of potential rate paths."
    }
}

# Main Content
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">Bond Market Analysis</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 2400px;">
            Comprehensive analysis of bond yields, interest rate dynamics, and market trends.
        </p>
    </div>
""", unsafe_allow_html=True)

# Quick Stats (Like first code, but bond-focused)
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="2Y Treasury", value="4.12%", delta="-0.03%")
with col2:
    st.metric(label="10Y Treasury", value="3.85%", delta="+0.05%")
with col3:
    st.metric(label="30Y Treasury", value="4.08%", delta="+0.02%")
with col4:
    st.metric(label="2Y-10Y Spread", value="-0.27%", delta="+0.08%")

# Main Navigation - Similar to first code, but bond-focused
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Yield Analysis", "Rate Forecasts", "Reports"])


def display_plots(plot_files, show_analysis=False):
    
    for plot_file in plot_files:
        if plot_file in PLOT_CONFIG:
            plot_path = os.path.join("plots", plot_file)
            try:
                with open(plot_path, "r", encoding='utf-8') as f:
                    html_content = f.read()
                
                st.markdown("""
                    <div style="background: #FFFFFF; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; border: 1px solid #E0E0E0;">
                """, unsafe_allow_html=True)
                st.info(PLOT_CONFIG[plot_file]["description"])
                components.html(html_content, height=PLOT_CONFIG[plot_file]["height"], width=2400)
                st.markdown('</div>', unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"Plot file not found: {plot_file}")

with tab1:
    # Filters Row
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        time_period = st.selectbox("Time Period", 
            ["1D", "1W", "1M", "3M", "6M", "1Y"])
    with col2:
        chart_type = st.selectbox("Chart Type",
            ["Line", "Area", "Scatter", "Bar"])
    with col3:
        indicators = st.multiselect("Technical Indicators",
            ["MA", "Bollinger", "RSI", "MACD"])
    with col4:
        st.selectbox("Export Options",
            ["PDF", "CSV", "Excel", "PNG"])

    # Add Market Insights Section
    st.markdown("""
        <div>
            <h2 style="color: #2E7D32; font-size: 2rem;">Market Insights</h2>
            <div class="insight-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1rem;">
                <div class="insight-card">
                    <div class="insight-title">Yield Curve Recovery</div>
                    <div class="insight-content">
                        The yield curve is showing significant recovery from its previous inversion state. 
                        Currently approaching a flattening point, with the 2Y-10Y spread at -0.27%, 
                        indicating potential economic stabilization.
                    </div>
                </div>
                <div class="insight-card">
                    <div class="insight-title">Rate Outlook</div>
                    <div class="insight-content">
                        Our interest rate forecasts suggest rates will maintain current levels in the near term. 
                        The CIR model and Monte Carlo simulations support this stability thesis.
                    </div>
                </div>
                <div class="insight-card">
                    <div class="insight-title">Key Implications</div>
                    <div class="insight-content">
                        <ul>
                            <li>Reduced recession risk signals from yield curve normalization</li>
                            <li>Stable rate environment supportive for fixed income positioning</li>
                            <li>Potential opportunity in intermediate duration bonds</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Show all plots in overview with analysis
    display_plots(PLOT_CONFIG.keys(), show_analysis=True)

with tab2:
    yield_plots = [f for f, config in PLOT_CONFIG.items() 
                   if config["category"] == "Yield Analysis"]
    display_plots(yield_plots, show_analysis=True)

with tab3:
    forecast_plots = [f for f, config in PLOT_CONFIG.items() 
                     if config["category"] == "Rate Forecasts"]
    display_plots(forecast_plots, show_analysis=True)

with tab4:
    st.markdown("### Reports")
    st.info("Bond market reports and documentation will be displayed here")

# Data Table Section
st.markdown("### Historical Data")
show_data = st.checkbox("Show Raw Data")
if show_data:
    st.dataframe({
        "Date": ["2024-01-22", "2024-01-21", "2024-01-20"],
        "10Y": [3.85, 3.80, 3.75],
        "2Y": [4.12, 4.15, 4.18],
        "Spread": [-0.27, -0.35, -0.43]
    })

# Footer
st.markdown("""
---
<div style="text-align: center; padding: 1rem;">
    <p style="color: #666666;">Data updated as of {}</p>
    <p style="color: #666666; font-size: 0.8rem;">
        Sources: Federal Reserve Economic Data (FRED), U.S. Treasury
    </p>
</div>
""".format(current_time.strftime('%Y-%m-%d %H:%M UTC')), unsafe_allow_html=True)