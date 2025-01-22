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

# CSS to scale content dynamically based on screen size
st.markdown("""
    <style>
        
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
            position: fixed;
            z-index: 99;
        }
        
        /* Market Insight Card Styles */
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
        
        /* Table styling */
        table.dataframe tbody tr:nth-child(odd) {
            background-color: #F8F9FA;
        }
        table.dataframe tbody tr:nth-child(even) {
            background-color: #FFFFFF;
        }
        table.dataframe thead th {
            font-size: 1rem;
            font-weight: bold;
            color: #2E7D32;
        }
        table.dataframe tbody td {
            font-size: 0.9rem;
            padding: 8px;
        }
        
        /* Plot container styles */
        .plot-container {
            width: 100%;
            margin: 0 auto;
            overflow: hidden;
        }
        
        .plot-container iframe {
            width: 100% !important;
            border: none !important;
        }
        
        /* Utility classes */
        .content-padding {
            padding: 1rem;
        }
        
        /* Remove column padding */
        .stColumns > div {
            padding: 0 !important;
        }
        
        /* Remove element margins */
        .element-container {
            margin: 0 !important;
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

# Function to create dynamic plot scaling
def create_plot_scaling_script():
    return """
        <script>
            function adjustPlotSize() {
                const plots = document.querySelectorAll('.plot-container iframe');
                plots.forEach(plot => {
                    const container = plot.parentElement;
                    const availableWidth = container.offsetWidth;
                    
                    // Calculate scale based on available width
                    const scale = availableWidth / 2400;
                    
                    // Apply the transform
                    plot.style.transform = `scale(${scale})`;
                    plot.style.transformOrigin = '0 0';
                    
                    // Adjust container height to match scaled content
                    const scaledHeight = plot.offsetHeight * scale;
                    container.style.height = `${scaledHeight}px`;
                });
            }
            
            // Run on load
            window.addEventListener('load', adjustPlotSize);
            
            // Run on resize
            window.addEventListener('resize', adjustPlotSize);
            
            // Additional trigger for Streamlit's dynamic updates
            new MutationObserver(function(mutations) {
                adjustPlotSize();
            }).observe(document.body, {
                attributes: true,
                childList: true,
                subtree: true
            });
        </script>
    """

# Modified load_html_plot function
def load_html_plot(plot_file, height=600):
    try:
        plot_path = os.path.join("plots", plot_file)
        with open(plot_path, 'r', encoding='utf-8') as f:
            plot_html = f.read()
            
            # Wrap plot in container with scaling
            responsive_plot = f"""
                <div class="plot-container">
                    {plot_html}
                </div>
                {create_plot_scaling_script()}
            """
            
            components.html(responsive_plot, height=height)
    except Exception as e:
        st.error(f"Unable to load plot: {str(e)}")
        st.info("Plot visualization is temporarily unavailable")

# Display plot
st.markdown("### Economic Health Score")
load_html_plot("Econ_Health_Score.html")

# Market data for tables
market_data = pd.DataFrame({
    "Market Sector": [
        "Communication Services", "Consumer Discretionary", "Consumer Staples",
        "Energy", "Financials", "Health Care", "Industrials", 
        "Information Technology", "Materials", "Real Estate", "Utilities"
    ],
    "Weighting in S&P 500 (%)": [8.2, 11.3, 5.5, 3.2, 13.6, 10.1, 9.4, 32.5, 1.9, 2.3, 2.1],
    "Trailing 6-Month Performance (%)": [7.6, 16.2, 2.0, 0.1, 13.9, -3.7, 8.7, -1.6, -5.0, 3.1, 10.6],
    "Trailing 12-Month Performance (%)": [38.6, 29.7, 11.3, 11.7, 27.2, 0.7, 18.7, 34.5, 1.3, 2.5, 21.2]
})

# Round all numeric values to 1 decimal place
market_data = market_data.round(1)

# Function to determine the color based on performance values
def get_performance_color(value):
    try:
        value = float(value)
        if value < 0:
            return f"background-color: rgba(255, 0, 0, {abs(value) / 100});"  # Red for negative values
        elif value > 0:
            return f"background-color: rgba(46, 125, 50, {value / 100});"  # Green for positive values
        else:
            return "background-color: #F8F9FA;"  # Neutral for zero values
    except ValueError:
        return "background-color: #F8F9FA;"

# Style the main table
styled_table = market_data.style.applymap(
    get_performance_color, subset=["Trailing 6-Month Performance (%)", "Trailing 12-Month Performance (%)"]
)

# Sort data for the right table
sorted_data = market_data.sort_values("Trailing 12-Month Performance (%)", ascending=False)

# Side-by-side tables with specified heights
col1, col2 = st.columns([2, 1], gap="small")

# Market Overview Table
with col1:
    st.markdown("### Market Overview")
    st.markdown(
        styled_table.format({
            "Weighting in S&P 500 (%)": "{:.1f}", 
            "Trailing 6-Month Performance (%)": "{:.1f}", 
            "Trailing 12-Month Performance (%)": "{:.1f}"
        }).to_html(),
        unsafe_allow_html=True
    )

# Sorted Performance Table
with col2:
    st.markdown("### Top Performers (Trailing 12-Month)")
    sorted_table = sorted_data[["Market Sector", "Trailing 12-Month Performance (%)"]].style.applymap(
        get_performance_color, subset=["Trailing 12-Month Performance (%)"]
    )
    st.markdown(
        sorted_table.format({"Trailing 12-Month Performance (%)": "{:.1f}"}).to_html(),
        unsafe_allow_html=True
    )


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



# Function to create plot scaling script
def create_plot_scaling_script():
    return """
        <script>
            function adjustPlotSize() {
                const plots = document.querySelectorAll('.plot-container iframe');
                plots.forEach(plot => {
                    const container = plot.parentElement;
                    const availableWidth = container.offsetWidth;
                    const scale = availableWidth / 2400;
                    
                    plot.style.transform = `scale(${scale})`;
                    plot.style.transformOrigin = '0 0';
                    
                    const scaledHeight = plot.offsetHeight * scale;
                    container.style.height = `${scaledHeight}px`;
                });
            }
            
            // Run on load
            window.addEventListener('load', adjustPlotSize);
            
            // Run on resize
            window.addEventListener('resize', adjustPlotSize);
            
            // Handle Streamlit's dynamic updates
            new MutationObserver(function(mutations) {
                adjustPlotSize();
            }).observe(document.body, {
                attributes: true,
                childList: true,
                subtree: true
            });
        </script>
    """

# Modified load_html_plot function
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

            # Wrap plot in responsive container with styling
            responsive_html = f"""
            <div class="plot-container">
                <div style="border: 1px solid #E0E0E0; border-radius: 12px; padding: 1rem; background-color: #FFFFFF;">
                    {plot_html}
                </div>
            </div>
            {create_plot_scaling_script()}
            """
            components.html(responsive_html, height=height)
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