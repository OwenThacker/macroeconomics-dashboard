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

        /* Sidebar Styles with Toggle */
        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
            transition: width 0.3s ease, transform 0.3s ease;
        }}

        /* Sidebar Toggle Styles */
        .sidebar-toggle {{
            position: absolute;
            top: 10px;
            right: 10px;
            cursor: pointer;
            z-index: 1000;
            background: #F0F0F0;
            border-radius: 50%;
            padding: 5px;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .sidebar-toggle svg {{
            width: 24px;
            height: 24px;
            fill: #2E7D32;
        }}

        /* Collapsed State */
        .collapsed [data-testid="stSidebar"] {{
            width: 0 !important;
            overflow: hidden;
            transform: translateX(-100%);
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
            background-image: url("{{image_base64}}");
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

        .plot-container {{
            margin-left: -50rem; /* Adjust this value to move left more or less */
            width: calc(100% 0rem); /* Compensate for the margin */
        }}

            
        <script>
        document.addEventListener('DOMContentLoaded', (event) => {{
            // Create toggle button
            const sidebarToggle = document.createElement('div');
            sidebarToggle.className = 'sidebar-toggle';
            sidebarToggle.innerHTML = `
                <svg viewBox="0 0 24 24">
                    <path d="M15.41 16.59L10.83 12l4.58-4.59L14 6l-6 6 6 6z"/>
                </svg>
            `;
            
            // Add click event to toggle sidebar
            sidebarToggle.addEventListener('click', () => {{
                document.body.classList.toggle('collapsed');
            }});
            
            // Find the sidebar and append the toggle button
            const sidebar = document.querySelector('[data-testid="stSidebar"]');
            if (sidebar) {{
                sidebar.appendChild(sidebarToggle);
            }}
        }});
        </script>

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

# Modified load_html_plot function
def load_html_plot(plot_file, height=1000):
    try:
        plot_path = os.path.join("plots", plot_file)
        with open(plot_path, 'r', encoding='utf-8') as f:
            html_content = f.read()
            
        st.markdown('<div class="plot-container">', unsafe_allow_html=True)
        html_base64 = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
        components.html(
            f"""
            <iframe src="data:text/html;base64,{html_base64}" 
                    width="2400" height="1200" style="border: none !important;"></iframe>
            """, 
            height=height
        )
        st.markdown('</div>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Plot '{plot_file}' not found.")
    except Exception as e:
        st.error(f"Error loading plot: {e}")

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

# Dynamically sized plot loading function
def load_html_plot(plot_name, max_width=3000, dynamic_height=True):
    try:
        plot_path = os.path.join("plots", f"{plot_name}.html")
        with open(plot_path, "r", encoding="utf-8") as f:
            plot_html = f.read()

        # Dynamic height adjustment based on content type
        height = 800  # Default height
        if dynamic_height:
            if "PCA" in plot_name:
                height = 2000
            elif "gdp" in plot_name or "voli" in plot_name or "vole" in plot_name or "inf" in plot_name or "unemp" in plot_name or "toti" in plot_name:
                height = 1200
            else:
                height = 1000

        # Embed the plot using an iframe with responsive width
        st.markdown('<div class="plot-container" style="overflow-x: auto;">', unsafe_allow_html=True)
        html_base64 = base64.b64encode(plot_html.encode('utf-8')).decode('utf-8')
        components.html(
            f"""
            <iframe src="data:text/html;base64,{html_base64}" 
                    width="100%" style="max-width:{max_width}px; border: none !important;" height="{height}">
            </iframe>
            """, 
            height=height
        )
        st.markdown('</div>', unsafe_allow_html=True)
    except FileNotFoundError:
        st.error(f"Plot '{plot_name}' not found.")
    except Exception as e:
        st.error(f"Error loading plot: {e}")

        st.error(f"Error loading plot: {e}")

# Display plot based on selection
st.markdown("""
    <div style="margin: 2rem 0;">
        <h3 style="color: #2E7D32; margin-bottom: 1rem;">Visualization</h3>
    </div>
""", unsafe_allow_html=True)

if selected_data_type == "PCA - Indicators Influence on Expenditures":
    plot_name = f"{selected_region}_PCA_I_E"
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