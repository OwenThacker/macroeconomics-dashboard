import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import os
import base64
import yfinance as yf
from fredapi import Fred
import plotly.graph_objects as go
import plotly.subplots as sp

# Configure Streamlit page
st.set_page_config(
    page_title="Alterra | Economic Overview Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# FRED API Configuration
secret_value_0 = "4ac2266ac7d9766069d3d0755561988a"  # Replace with your FRED API key
fred = Fred(api_key=secret_value_0)

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

# Main Content
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">S&P 500 Analysis</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 2400px;">
            Explore interactive visualizations of economic trends and asset behavior across various market conditions.
        </p>
    </div>
""", unsafe_allow_html=True)

# Fetching live data

sp500 = yf.Ticker('^GSPC')
sp500_hist = sp500.history(period='max')
sp500_close = sp500_hist['Close']
latest_price = sp500_close.iloc[-1]
pct_change = sp500_close.pct_change()
latest_pct_change = pct_change.iloc[-1] * 100
# Calculate the Log Returns
log_returns = np.log(sp500_close / sp500_close.shift(1))

# Calculate the rolling yearly volatility (252 trading days in a year)
yearly_volatility = log_returns.rolling(window=252).std() * np.sqrt(252)  # Annualizing volatility

# Calculate the percentage change of the Volume
volume_pct_change = sp500_hist["Volume"].pct_change(365) * 100  # Volume pct change from a year ago


# Retrieve data from FRED
gdp_data = fred.get_series('GDPC1')  # Real GDP
inflation_data = fred.get_series('CPIAUCSL')  # Inflation (CPI)
unemployment_data = fred.get_series('UNRATE')  # Unemployment

# Fill missing data (NaN) using forward fill or interpolation
gdp_data = gdp_data.fillna(method='ffill')  # Forward fill missing GDP data
inflation_data = inflation_data.fillna(method='ffill')  # Forward fill missing Inflation data
unemployment_data = unemployment_data.fillna(method='ffill')  # Forward fill missing Unemployment data

# Resample data to daily frequency (if needed, otherwise skip this part)
gdp_data = gdp_data.resample('D').ffill()  # Resample to daily and forward fill missing values
inflation_data = inflation_data.resample('D').ffill()  # Resample to daily and forward fill missing values
unemployment_data = unemployment_data.resample('D').ffill()  # Resample to daily and forward fill missing values

# Calculate Year-over-Year (YoY) Growth: Percentage change from 365 days ago
latest_gdp_yoy = round(gdp_data.pct_change(365).iloc[-1] * 100, 2)  # GDP YoY Growth
latest_inf_yoy = round(inflation_data.pct_change(365).iloc[-1] * 100, 2)  # Inflation YoY Growth

# Calculate Daily Percentage Change (Delta) from the previous day
latest_gdp_pct = round(gdp_data.pct_change().iloc[-1] * 100, 2)  # Daily GDP Percentage Change
latest_inf_pct = round(inflation_data.pct_change().iloc[-1] * 100, 2)  # Daily Inflation Percentage Change

# Get the latest values for GDP, Inflation, and Unemployment
latest_gdp = round(gdp_data.iloc[-1], 2)  # Latest GDP value
latest_inf = round(inflation_data.iloc[-1], 2)  # Latest Inflation value
latest_unemp = round(unemployment_data.iloc[-1], 2)  # Latest Unemployment rate

# Get the daily percentage change for Unemployment
latest_unemp_pct = round(unemployment_data.pct_change().iloc[-1] * 100, 2)  # Daily Unemployment Percentage Change


# Quick Stats
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric(label="S&P 500", value=f"{latest_price:.2f}", delta=f"{latest_pct_change:.2f}%")  # Replace with actual S&P 500 values
with col2:
    st.metric(label="GDP Growth (YoY)", value=f"{latest_gdp_yoy}%", delta=f"{latest_gdp_pct}%")
with col3:
    st.metric(label="Inflation Rate (YoY)", value=f"{latest_inf_yoy}%", delta=f"{latest_inf_pct}%")
with col4:
    st.metric(label="Unemployment", value=f"{latest_unemp}%", delta=f"{latest_unemp_pct}%")


# Main Navigation with SP500 tab moved second
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "SP500", "Economic Indicators", "Market Analysis", "Reports"])

with tab1:

    # Plot Categories
    plot_category = st.selectbox(
        "Select Analysis Category",
        ["GDP Analysis", "Inflation Metrics", "Employment Data", "Interest Rates", "SP500"]
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


with tab2:  # SP500 Tab (Second)
    # Filter data from 1960 onwards
    start_date = '1960-01-01'
    filtered_data = sp500_hist[sp500_hist.index >= start_date]
    filtered_returns = log_returns[log_returns.index >= start_date]
    filtered_volatility = yearly_volatility[yearly_volatility.index >= start_date]
    filtered_volume_change = volume_pct_change[volume_pct_change.index >= start_date]

    # Create subplots vertically
    fig = sp.make_subplots(
        rows=4, cols=1,
        subplot_titles=(
            "S&P 500 Price",
            "S&P 500 Log Returns (%)",
            "S&P 500 Yearly Volatility (%)",
            "S&P 500 Volume % Change"
        ),
        vertical_spacing=0.08,
        specs=[[{"type": "scatter"}], [{"type": "scatter"}], 
               [{"type": "scatter"}], [{"type": "scatter"}]]
    )

    # S&P 500 Price Plot
    fig.add_trace(
        go.Scatter(
            x=filtered_data.index,
            y=filtered_data['Close'],
            mode='lines',
            name='S&P 500',
            line=dict(
                color='rgb(0, 91, 150)',
                width=1.5
            ),
            fill='tonexty',
            fillcolor='rgba(0, 91, 150, 0.1)'
        ),
        row=1, col=1
    )

    # Log Returns Plot
    fig.add_trace(
        go.Scatter(
            x=filtered_returns.index,
            y=filtered_returns * 100,
            mode='lines',
            name='Log Returns',
            line=dict(
                color='rgb(49, 130, 189)',
                width=1.5
            ),
            fill='tonexty',
            fillcolor='rgba(49, 130, 189, 0.1)'
        ),
        row=2, col=1
    )

    # Yearly Volatility Plot
    fig.add_trace(
        go.Scatter(
            x=filtered_volatility.index,
            y=filtered_volatility * 100,
            mode='lines',
            name='Yearly Volatility',
            line=dict(
                color='rgb(50, 171, 96)',
                width=1.5
            ),
            fill='tonexty',
            fillcolor='rgba(50, 171, 96, 0.1)'
        ),
        row=3, col=1
    )

    # Volume % Change Plot
    fig.add_trace(
        go.Scatter(
            x=filtered_volume_change.index,
            y=filtered_volume_change,
            mode='lines',
            name='Volume % Change',
            line=dict(
                color='rgb(189, 49, 49)',
                width=1.5
            ),
            fill='tonexty',
            fillcolor='rgba(189, 49, 49, 0.1)'
        ),
        row=4, col=1
    )

    # Update layout for better visibility
    fig.update_layout(
        template='plotly_white',
        height=1200,  # Increased height for 4 plots
        width=2400,
        title=dict(
            text="S&P 500 Market Analysis Dashboard (1960 - Present)",
            x=0.5,
            y=0.95,
            font=dict(size=24)
        ),
        showlegend=False,
        margin=dict(t=120, l=50, r=50, b=50)
    )

    # Update axes
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128, 128, 128, 0.2)',
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='rgba(128, 128, 128, 0.5)'
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128, 128, 128, 0.2)',
        zeroline=True,
        zerolinewidth=1,
        zerolinecolor='rgba(128, 128, 128, 0.5)'
    )

    # Update hover templates separately for each plot
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x}<br>" +
                      "<b>Value</b>: %{y:.2f}<br>",
        row=1
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x}<br>" +
                      "<b>Value</b>: %{y:.2f}%<br>",
        row=2
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x}<br>" +
                      "<b>Value</b>: %{y:.2f}%<br>",
        row=3
    )
    
    fig.update_traces(
        hovertemplate="<b>Date</b>: %{x}<br>" +
                      "<b>Value</b>: %{y:.2f}%<br>",
        row=4
    )

    # Show plot in Streamlit
    st.plotly_chart(fig, use_container_width=True)

with tab3:  # Economic Indicators Tab
    st.markdown("### Economic Indicators Analysis")
    st.info("Economic indicators analysis content will be displayed here.")

with tab4:  # Market Analysis Tab
    st.markdown("### Market Analysis")
    st.info("Market analysis content will be displayed here.")

with tab5:  # Reports Tab
    st.markdown("### Reports")
    st.info("Reports and documentation will be displayed here.")

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