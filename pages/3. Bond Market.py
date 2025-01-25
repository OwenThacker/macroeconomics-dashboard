import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import os
import base64
import plotly.graph_objects as go
import plotly.io as pio

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

# Extend the tab navigation
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Overview", "Yield Analysis", "Rate Forecasts", "Scenario Analysis", "Reports"])

# Logic for each tab
with tab1:
    # Logic for the "Overview" tab
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        time_period = st.selectbox("Time Period", ["1D", "1W", "1M", "3M", "6M", "1Y"])
    with col2:
        chart_type = st.selectbox("Chart Type", ["Line", "Area", "Scatter", "Bar"])
    with col3:
        indicators = st.multiselect("Technical Indicators", ["MA", "Bollinger", "RSI", "MACD"])
    with col4:
        st.selectbox("Export Options", ["PDF", "CSV", "Excel", "PNG"])
    display_plots(PLOT_CONFIG.keys(), show_analysis=True)

with tab2:
    # Logic for the "Yield Analysis" tab
    yield_plots = [f for f, config in PLOT_CONFIG.items() if config["category"] == "Yield Analysis"]
    display_plots(yield_plots, show_analysis=True)

with tab3:
    # Logic for the "Rate Forecasts" tab
    forecast_plots = [f for f, config in PLOT_CONFIG.items() if config["category"] == "Rate Forecasts"]
    display_plots(forecast_plots, show_analysis=True)

# New Scenario Analysis Tab
with tab4:
    st.markdown("""
        <h2 style="color: #2E7D32; font-size: 2rem;">Scenario Analysis</h2>
        <p style="color: #666666; font-size: 1.2rem;">
            Model how random shocks to yield curve factors (e.g., Wiggle, Flex, Twist, Shift) 
            propagate their impacts across the treasury rates.
        </p>
    """, unsafe_allow_html=True)

    # Sidebar-like controls for Scenario Analysis
    col1, col2, col3 = st.columns(3)
    with col1:
        volatility = st.number_input("Volatility (Standard Deviation)", value=1.0, step=0.1, format="%.2f", min_value=0.01)
    with col2:
        distribution_type = st.selectbox("Shock Distribution Type", ["Normal", "Uniform"])
    with col3:
        num_simulations = st.number_input("Number of Simulations", min_value=100, max_value=5000, value=1000, step=100)

    # Generate Random Shock Vector
    def generate_shocks(volatility, size, distribution_type):
        if distribution_type == "Normal":
            return np.random.normal(0, volatility, size=size)
        elif distribution_type == "Uniform":
            return np.random.uniform(-volatility, volatility, size=size)

    # Create a placeholder covariance matrix and transformation matrix
    np.random.seed(42)  # For reproducibility
    rates_columns = ["1Y", "2Y", "5Y", "10Y", "30Y"]
    C = np.cov(np.random.rand(5, len(rates_columns)))  # Example covariance matrix
    eigenvalues, eigenvectors = np.linalg.eig(C)
    lambda_sqrt = np.sqrt(eigenvalues)
    eigv_decomp = np.diag(lambda_sqrt)
    B = eigv_decomp @ eigenvectors.T
    B = pd.DataFrame(data=B[:4] * 100, index=["Wiggle", "Flex", "Twist", "Shift"], columns=rates_columns)

    # Run multiple simulations and store results
    all_impacts = []
    for _ in range(num_simulations):
        Random_Shock = generate_shocks(volatility=volatility, size=(4,), distribution_type=distribution_type)
        impacts = Random_Shock @ B.values
        all_impacts.append(impacts)

    # Convert impacts to a numpy array for easier manipulation
    all_impacts = np.array(all_impacts)

    # Calculate the mean and standard deviation of the impacts
    avg_impacts = np.mean(all_impacts, axis=0)
    std_impacts = np.std(all_impacts, axis=0)


    # Create a sophisticated color palette
    colors = ['#2E7D32', '#388E3C', '#43A047', '#4CAF50', '#66BB6A']

    # Create figure with subplots for more detailed visualization
    fig = go.Figure()

    # Average Impact Trace with sophisticated styling
    fig.add_trace(
        go.Bar(
            x=rates_columns,
            y=avg_impacts,
            name='Average Impact',
            text=[f"{val:.2f}" for val in avg_impacts],
            textposition='outside',
            marker=dict(
                color=colors,
                line=dict(color='darkgreen', width=1.5),
                opacity=0.8
            ),
            hovertemplate='<b>%{x}</b><br>Avg Impact: %{y:.2f} bps<extra></extra>',
            width=0.6
        )
    )

    # Standard Deviation Trace
    fig.add_trace(
        go.Scatter(
            x=rates_columns,
            y=std_impacts,
            mode='markers+lines',
            name='Std Deviation',
            line=dict(color='rgba(46, 125, 50, 0.5)', dash='dot', width=2),
            marker=dict(
                color='rgba(46, 125, 50, 0.7)', 
                size=10, 
                symbol='diamond',
                line=dict(color='darkgreen', width=1.5)
            ),
            hovertemplate='<b>%{x}</b><br>Std Dev: %{y:.2f} bps<extra></extra>'
        )
    )

    # Enhanced layout
    fig.update_layout(
        title={
            'text': 'Impact of Random Shocks on Treasury Rates',
            'y':0.95,
            'x':0.5,
            'xanchor': 'center', 
            'yanchor': 'top',
            'font': dict(size=24, color='#2E7D32')
        },
        xaxis_title='Treasury Rates',
        yaxis_title='Impact (Basis Points)',
        template='plotly_white',
        width=2800,  # Wide format
        height=600,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5
        ),
        plot_bgcolor='rgba(240,248,255,0.5)',
        paper_bgcolor='white',
    )

    # Style enhancements
    fig.update_xaxes(
        showline=True, 
        linewidth=2, 
        linecolor='lightgray', 
        gridcolor='lightgray'
    )
    fig.update_yaxes(
        showline=True, 
        linewidth=2, 
        linecolor='lightgray', 
        gridcolor='lightgray'
    )

    # Display the Plotly chart
    st.plotly_chart(fig, use_container_width=False)

    # Optionally show the transformation matrix
    if st.checkbox("Show Transformation Matrix"):
        st.dataframe(B)

    # Optionally display raw shock values for the first simulation
    if st.checkbox("Show Raw Shocks (First Simulation)"):
        st.write("Random Shock Vector (First Simulation):", all_impacts[0])


with tab5:
    # Logic for the "Reports" tab
    st.markdown("### Reports")
    st.info("Bond market reports and documentation will be displayed here")


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