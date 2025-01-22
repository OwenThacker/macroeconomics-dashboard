import streamlit as st
import streamlit.components.v1 as components
import os
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="Bond Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar CSS
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
            width: 250px;
        }
        
        .stSidebar h1 {
            font-size: 1.8rem;
            font-weight: 600;
            color: #2E7D32;
            text-align: center;
        }

        .stSidebar p {
            color: #90A4AE;
            margin-top: 0.5rem;
            text-align: center;
        }

        .insight-card {
            background: #FFFFFF;
            border-radius: 12px;
            padding: 1.5rem;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            cursor: pointer;
            margin-bottom: 1rem;
        }

        .insight-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }

        .insight-title {
            font-size: 1.2rem;
            color: #2E7D32;
            font-weight: 600;
        }

        .insight-content {
            font-size: 1.0rem;
            color: #262626;
            margin-top: 0.5rem;
        }

        .insight-footer {
            font-size: 0.9rem;
            color: #90A4AE;
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }

        .insight-impact {
            color: #2E7D32;
            font-weight: 600;
        }

        .market-status {
            background: #F8F9FA;
            padding: 1rem;
            border-radius: 8px;
            margin: 1rem 0;
            font-size: 0.9rem;
        }
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

    # Bond Market Insights
    st.markdown("### Market Insights", unsafe_allow_html=True)
    insights = [
        {
            "title": "Yield Curve Alert",
            "content": "10Y-2Y spread widens to -27 bps",
            "trend": "↗️ Steepening",
            "impact": "High"
        },
        {
            "title": "Treasury Update",
            "content": "30Y yields show 5% weekly increase",
            "trend": "↗️ Rising",
            "impact": "Medium"
        },
        {
            "title": "Rate Outlook",
            "content": "Fed futures predict steady rates",
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

# Main Content Area
st.markdown("""
    <div class="hero-container">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">
            Bond Analysis Dashboard
        </h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            Comprehensive analysis of yield curves and bond market indicators.
        </p>
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
        "height": 600,
        "category": "Rate Forecasts",
        "description": "Cox-Ingersoll-Ross model predictions for rate behavior."
    },
    "CIR_Model_MonteCarlo_Hist.html": {
        "height": 600,
        "category": "Rate Forecasts",
        "description": "Monte Carlo simulations of potential rate paths."
    }
}

def display_market_analysis():
    st.markdown("""
    ### Current Market Analysis
    """)

    analysis_container = st.container()
    with analysis_container:
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Yield Curve Recovery")
            st.write("The yield curve is showing significant recovery from its previous inversion state. Currently approaching a flattening point, with the 2Y-10Y spread at -0.27%, indicating potential economic stabilization.")
            
            st.subheader("Rate Outlook")
            st.write("Our interest rate forecasts suggest rates will maintain current levels in the near term. The CIR model and Monte Carlo simulations support this stability thesis.")

        with col2:
            st.subheader("Key Implications")
            st.write("• Reduced recession risk signals from yield curve normalization")
            st.write("• Stable rate environment supportive for fixed income positioning")
            st.write("• Potential opportunity in intermediate duration bonds")

def display_plots(plot_files, show_analysis=False):
    if show_analysis:
        display_market_analysis()
    
    for plot_file in plot_files:
        if plot_file in PLOT_CONFIG:
            plot_path = os.path.join("plots", plot_file)
            try:
                with open(plot_path, "r", encoding='utf-8') as f:
                    html_content = f.read()
                
                st.markdown("""
                    <div style="background: #FFFFFF; padding: 1.5rem; border-radius: 8px; margin: 1rem 0; border: 1px solid #E0E0E0;">
                """, unsafe_allow_html=True)
                st.markdown(f"### {plot_file.replace('.html', '').replace('_', ' ').title()}")
                st.info(PLOT_CONFIG[plot_file]["description"])
                components.html(html_content, height=PLOT_CONFIG[plot_file]["height"])
                st.markdown('</div>', unsafe_allow_html=True)
            except FileNotFoundError:
                st.error(f"Plot file not found: {plot_file}")

# Main Navigation
tab1, tab2, tab3, tab4 = st.tabs(["Overview", "Yield Analysis", "Rate Forecasts", "Reports"])

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

    # KPI Cards with reordered metrics
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="2Y Treasury", value="4.12%", delta="-0.03%")
    with col2:
        st.metric(label="10Y Treasury", value="3.85%", delta="+0.05%")
    with col3:
        st.metric(label="30Y Treasury", value="4.08%", delta="+0.02%")
    with col4:
        st.metric(label="2Y-10Y Spread", value="-0.27%", delta="+0.08%")

    # Show all plots in overview
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