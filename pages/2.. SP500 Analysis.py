import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="SP500 Analysis",
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
    # Sidebar Title
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

    # Generate Insight Cards
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
            SP500 Analysis
        </h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            Comprehensive analysis of SP500 and economic indicators for informed decision-making.
        </p>
    </div>
""", unsafe_allow_html=True)

# Main Navigation
st.markdown('<div class="nav-container">', unsafe_allow_html=True)
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

    # KPI Summary Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="S&P 500", value="6,049.24", delta="1,198.81 (24.72%) Past Year")
    with col2:
        st.metric(label="GDP Growth", value="2.5%", delta="0.3%")
    with col3:
        st.metric(label="Inflation Rate", value="3.4%", delta="-0.1%")
    with col4:
        st.metric(label="Unemployment", value="3.7%", delta="0.0%")

    # Plot Categories
    plot_category = st.selectbox(
        "Select Analysis Category",
        ["GDP Analysis", "Inflation Metrics", "Employment Data", "Interest Rates"]
    )

    # Define plot descriptions
    PLOT_DESCRIPTIONS = {
        "sp500_gdp_mom.html": """
            Strong correlation between S&P 500 performance and U.S. GDP growth.
            Historical data shows GDP as a useful indicator for market positioning.
        """,
        "sp500_cpi_mom.html": """
            Correlation between S&P 500 and CPI shows upward trend with moderate alignment.
            Other factors should be considered in analysis.
        """,
        "sp500_ppi_mom.html": """
            Looser correlation observed. PPI impacts inflation trends but shows
            inconsistent relationship with S&P 500.
        """,
        "sp500_unemp_mom.html": """
            Limited correlation between unemployment figures and S&P 500 performance.
            Momentum indicator serves as confirmation tool.
        """,
        "sp500_ir_mom.html": """
            Strong correlation between interest rates and S&P 500 performance.
            Interest rates often serve as leading indicator.
        """
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
            
            st.markdown('<div class="plot-container">', unsafe_allow_html=True)
            st.markdown(f"### {plot_file.replace('.html', '').replace('_', ' ').title()}")
            if plot_file in PLOT_DESCRIPTIONS:
                st.info(PLOT_DESCRIPTIONS[plot_file])
            components.html(html_content, height=800)
            st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown("### Economic Indicators Analysis")
    # Add economic indicators content here
    st.info("Economic indicators analysis content will be displayed here")

with tab3:
    st.markdown("### Market Analysis")
    # Add market analysis content here
    st.info("Market analysis content will be displayed here")

with tab4:
    st.markdown("### Reports")
    # Add reports content here
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