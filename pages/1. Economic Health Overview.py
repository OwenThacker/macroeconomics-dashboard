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

# Updated styling that focuses on the sidebar while preserving your existing styles
st.markdown("""
    <style>
        /* Sidebar Styles */
        [data-testid="stSidebar"] {
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
        }
        
        .main {
            background-color: #FFFFFF;
        }
        
        /* Market Insight Card Styles for Sidebar */
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

# Main Content Header
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">Economic Overview Dashboard</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            Advanced analytics and real-time market insights for informed decision-making
        </p>
    </div>
""", unsafe_allow_html=True)

# Key Metrics Row
col1, col2, col3, col4 = st.columns(4)
metrics = [
    {"label": "Global Economic Score", "value": "94.2", "delta": "+2.1"},
    {"label": "Market Volatility", "value": "18.5%", "delta": "-3.2"},
    {"label": "Trading Volume", "value": "$2.8T", "delta": "+15%"},
    {"label": "Active Markets", "value": "142", "delta": "+3"}
]

for col, metric in zip([col1, col2, col3, col4], metrics):
    with col:
        st.markdown(f"""
            <div class="metric-card">
                <div style="color: #90A4AE; font-size: 0.9rem;">{metric['label']}</div>
                <div style="font-size: 1.8rem; font-weight: 600; color: #2E7D32;">{metric['value']}</div>
                <div style="color: {'#2E7D32' if float(metric['delta'].replace('%','').replace('$','').replace('+','')) > 0 else '#FF5252'}; font-size: 0.9rem; margin-top: 0.5rem;">
                    {metric['delta']}
                </div>
            </div>
        """, unsafe_allow_html=True)

# Improved Plot display
def load_html_plot(plot_file, height=600):
    try:
        plot_path = os.path.join("plots", plot_file)
        with open(plot_path, 'r', encoding='utf-8') as f:
            plot_html = f.read()
            components.html(plot_html, height=height)
    except Exception as e:
        st.error(f"Unable to load plot: {str(e)}")
        st.info("Plot visualization is temporarily unavailable")

# Display plot
st.markdown("### Economic Health Score")
load_html_plot("Econ_Health_Score.html")

# Function to determine the color based on performance values
def get_performance_color(value):
    try:
        value = float(value)
        # Apply color gradient from dark red to dark green
        if value < 0:
            return f"background-color: rgba(255, 0, 0, {abs(value) / 100})"  # Dark red for negative values
        elif value > 0:
            return f"background-color: rgba(46, 125, 50, {value / 100})"  # Dark green for positive values
        else:
            return "background-color: #F8F9FA;"  # Neutral color for zero values
    except ValueError:
        return "background-color: #F8F9FA;"  # Default for invalid data

# Market Overview Table with color-coded returns
st.markdown("""
    <div style="margin: 2rem 0;">
        <h3 style="color: #262626; margin-bottom: 1rem;">Market Overview</h3>
        <table class="styled-table">
            <thead>
                <tr>
                    <th>Market Sector</th>
                    <th>Weighting in S&P 500 (%)</th>
                    <th>Trailing 6-Month Performance (%)</th>
                    <th>Trailing 12-Month Performance (%)</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Communication Services</td>
                    <td>8.2</td>
                    <td style="{}">7.6</td>
                    <td style="{}">38.6</td>
                </tr>
                <tr>
                    <td>Consumer Discretionary</td>
                    <td>11.3</td>
                    <td style="{}">16.2</td>
                    <td style="{}">29.7</td>
                </tr>
                <tr>
                    <td>Consumer Staples</td>
                    <td>5.5</td>
                    <td style="{}">2.0</td>
                    <td style="{}">11.3</td>
                </tr>
                <tr>
                    <td>Energy</td>
                    <td>3.2</td>
                    <td style="{}">0.1</td>
                    <td style="{}">11.7</td>
                </tr>
                <tr>
                    <td>Financials</td>
                    <td>13.6</td>
                    <td style="{}">13.9</td>
                    <td style="{}">27.2</td>
                </tr>
                <tr>
                    <td>Health Care</td>
                    <td>10.1</td>
                    <td style="{}">-3.7</td>
                    <td style="{}">0.7</td>
                </tr>
                <tr>
                    <td>Industrials</td>
                    <td>9.4</td>
                    <td style="{}">8.7</td>
                    <td style="{}">18.7</td>
                </tr>
                <tr>
                    <td>Information Technology</td>
                    <td>32.5</td>
                    <td style="{}">-1.6</td>
                    <td style="{}">34.5</td>
                </tr>
                <tr>
                    <td>Materials</td>
                    <td>1.9</td>
                    <td style="{}">-5.0</td>
                    <td style="{}">1.3</td>
                </tr>
                <tr>
                    <td>Real Estate</td>
                    <td>2.3</td>
                    <td style="{}">3.1</td>
                    <td style="{}">2.5</td>
                </tr>
                <tr>
                    <td>Utilities</td>
                    <td>2.1</td>
                    <td style="{}">10.6</td>
                    <td style="{}">21.2</td>
                </tr>
                <tr>
                    <td><strong>S&P 500 Index</strong></td>
                    <td>100.0</td>
                    <td style="{}"><strong>4.1</strong></td>
                    <td style="{}"><strong>23.5</strong></td>
                </tr>
            </tbody>
        </table>
    </div>
""".format(
    get_performance_color(7.6), get_performance_color(38.6),
    get_performance_color(16.2), get_performance_color(29.7),
    get_performance_color(2.0), get_performance_color(11.3),
    get_performance_color(0.1), get_performance_color(11.7),
    get_performance_color(13.9), get_performance_color(27.2),
    get_performance_color(-3.7), get_performance_color(0.7),
    get_performance_color(8.7), get_performance_color(18.7),
    get_performance_color(-1.6), get_performance_color(34.5),
    get_performance_color(-5.0), get_performance_color(1.3),
    get_performance_color(3.1), get_performance_color(2.5),
    get_performance_color(10.6), get_performance_color(21.2),
    get_performance_color(4.1), get_performance_color(23.5)
), unsafe_allow_html=True)


# Dropdown for Data Type Selection
data_type_options = [
    "Regional GDP",
    "Regional Volume of Imports of Goods",
    "Regional Volume of Exports of Goods",
    "Regional Inflation, Average CPI",
    "Regional Unemployment Rate",
    "Regional Total Investment",
    "Regional Expenditure",
    "PCA - Indicators Influence on Expenditures"
]

# Dropdown Section with Improved Styling (no background box around titles)
st.markdown("""
    <div style="margin: 0rem 0 0.2rem 0; padding: 0rem 1rem; border: 0px solid #E0E0E0; border-radius: 8px; background-color: #F8F9FA;">
        <p style="color: #2E7D32; font-size: 1.2rem; font-weight: 600; margin-bottom: 0.2rem; margin-left: -1rem;">Select Data Type</p>
    </div>
""", unsafe_allow_html=True)

# Dropdown for Data Type Selection
selected_data_type = st.selectbox(
    "Choose the type of data visualization:",
    data_type_options,
    key="data_type_selector"
)

# Conditional Dropdown for PCA Regions
if selected_data_type == "PCA - Indicators Influence on Expenditures":
    st.markdown("""
        <div style="margin-top: 0.5rem; padding: 0rem 1rem; border: 0px solid #E0E0E0; border-radius: 8px; background-color: #FFFFFF;">
            <p style="color: #2E7D32; font-size: 1.2rem; font-weight: 600; margin-bottom: 0.2rem; margin-left: -1rem;">Select Region</p>
        </div>
    """, unsafe_allow_html=True)
    region_options = ["Oceania", "Europe", "South America", "Asia", "North America", "Africa"]
    selected_region = st.selectbox(
        "Choose the region for PCA analysis:",
        region_options,
        key="region_selector"
    )


# Function to load HTML plots with consistent styling
def load_html_plot(plot_name):
    try:
        plot_path = os.path.join("plots", f"{plot_name}.html")
        with open(plot_path, "r", encoding="utf-8") as f:
            plot_html = f.read()

            # Dynamic height adjustment
            if "PCA" in plot_name:
                height = 2200
            elif "gdp" in plot_name or "voli" in plot_name or "vole" in plot_name or "inf" in plot_name or "unemp" in plot_name or "toti" in plot_name:
                height = 1600
            else:
                height = 3000

            # Styled HTML wrapper for consistency
            styled_html = f"""
            <div style="width: 100%; max-width: 2400px; margin: 0 auto; border: 1px solid #E0E0E0; border-radius: 12px; padding: 1rem; background-color: #FFFFFF;">
                {plot_html}
            </div>
            """
            components.html(styled_html, height=height)
    except FileNotFoundError:
        st.error(f"Plot '{plot_name}' not found.")
    except Exception as e:
        st.error(f"Error loading plot: {e}")

# Display plot based on selection
st.markdown("""
    <div style="margin: 2rem 0;">
        <h3 style="color: #2E7D32; margin-bottom: 1rem;">Visualization</h3>
    </div>
""", unsafe_allow_html=True)

if selected_data_type == "PCA - Indicators Influence on Expenditures":
    plot_name = f"{selected_region.lower()}_PCA_I_E"
    st.write(f"Displaying PCA analysis for **{selected_region}**.")
    load_html_plot(plot_name)
else:
    plot_mapping = {
        "Regional GDP": "Regional_gdp",
        "Regional Volume of Imports of Goods": "Regional_voli",
        "Regional Volume of Exports of Goods": "Regional_vole",
        "Regional Inflation, Average CPI": "Regional_inf",
        "Regional Unemployment Rate": "Reigonal_unemp",
        "Regional Total Investment": "Regional_toti",
        "Regional Expenditure": "Regional_expenditure"
    }
    plot_name = plot_mapping[selected_data_type]
    st.write(f"Displaying **{selected_data_type}** data visualization.")
    load_html_plot(plot_name)

st.markdown('</div>', unsafe_allow_html=True)


# Footer
st.markdown(f"""
    <div style="background: #F8FAFC; padding: 2rem; margin-top: 3rem; text-align: center; border-top: 1px solid #E0E0E0;">
        <div style="color: #90A4AE; font-size: 0.9rem;">Powered by</div>
        <div style="color: #2E7D32; font-size: 1.2rem; font-weight: 600; margin-top: 0.5rem;">ALTERRA</div>
        <div style="color: #90A4AE; font-size: 0.8rem; margin-top: 1rem;">
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
    </div>
""", unsafe_allow_html=True)