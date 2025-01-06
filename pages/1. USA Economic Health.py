import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Page configuration
st.set_page_config(
    page_title="Economic Health Dashboard",
    layout="wide"
)

# Apply custom CSS for consistent styling across all dashboards
st.markdown(
    """
    <style>
        /* General page styling */
        body {
            zoom: 90%;
            margin: 0;
            padding: 0;
            overflow-x: hidden; /* Prevent horizontal scroll */
        }
        .main .block-container {
            max-width: 2500px;
            padding-left: 0rem;
            padding-right: 0rem;
            margin-left: 0;
            margin-right: 0;
        }
        
        /* Page title styling */
        h1 {
            color: #8BC34A;
            font-size: 2.0em; /* Largest text for the main title */
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Section title styling */
        .section-title {
            font-size: 1.6em; /* Clear and bold subtitle */
            font-weight: bold;
            margin-top: 20px;
            margin-bottom: 10px;
        }

        /* Description container */
        .description-container {
            padding: 12px;
            margin-bottom: 20px;
            background-color: #f9fafb;
            border-left: 4px solid #1f77b4;
            font-size: 1.0em; /* Smaller, readable text */
            line-height: 1.5;
        }

        /* General text styling */
        p, li, div {
            font-size: 1.05em; /* Default text size for normal content */
            line-height: 1.5;
        }
        
        /* Plot container */
        .plot-container {
            width: 100%;
            margin-bottom: 30px;
            border: 1px solid #ddd;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            overflow-x: hidden; /* Prevent iframe from causing horizontal scroll */
        }

        /* Ensure iframe fits perfectly */
        iframe {
            display: block;
            margin: 0 auto;
            width: 100%;
            max-width: 100%;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Plot descriptions
PLOT_DESCRIPTIONS = {
    "Econ_Health_Score.html": "The Economic Health Score provides a concise overview of the economy's current state, indicating positive economic fundamentals and sustained growth momentum.",
    "DGDP_Ratio.html": "The Debt-to-GDP ratio shows a manageable upward trajectory, indicating controlled debt management and fiscal stability.",
    "usa_revenue.html": "Revenue trends demonstrate steady Month-over-Month growth, supporting fiscal health and stability.",
    "Interest_Cov_Ratio.html": "Improvement in Interest Coverage Ratio indicates efficient debt management and stronger fiscal health.",
    "usa_sur_def.html": "Improvement in the surplus/deficit position highlights effective fiscal management and financial stability."
}

# Page title
st.title("USA Economic Health Dashboard")

st.write("""
This dashboard offers key insights into economic health indicators through interactive visualizations. 
Key metrics such as Debt-to-GDP, revenue trends, and fiscal surplus/deficit are presented for analysis.
""")

# Plot details with individual dimensions (width and height)
PLOT_FILES = [
    ("Econ_Health_Score.html", "Economic Health Score", "100%", 400),
    ("DGDP_Ratio.html", "Debt-to-GDP Ratio", "100%", 650),
    ("usa_revenue.html", "USA Revenue", "100%", 650),
    ("Interest_Cov_Ratio.html", "Interest Coverage Ratio", "100%", 650),
    ("usa_sur_def.html", "USA Surplus/Deficit", "100%", 650)
]

PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display plots with individual dimensions and descriptions
for plot_file, plot_title, max_width, max_height in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "r", encoding="utf-8") as f:
            html_content = f.read()
        
        st.markdown(f"### {plot_title}")
        
        # Add description with styled container
        if plot_file in PLOT_DESCRIPTIONS:
            st.markdown(f"""
                <div style='
                    padding: 15px;
                    margin-bottom: 25px;
                    background-color: #f8f9fa;
                    border-left: 4px solid #1f77b4;
                    font-size: 0.95em;
                    line-height: 1.6;
                '>
                    {PLOT_DESCRIPTIONS[plot_file]}
                </div>
            """, unsafe_allow_html=True)
        
        # Encode HTML content as base64
        html_base64 = base64.b64encode(html_content.encode('utf-8')).decode('utf-8')
        
        # Display the plot with individual dimensions
        st.components.v1.html(
            f"""
            <iframe src="data:text/html;base64,{html_base64}" 
                    width="{max_width}" height="{max_height}" 
                    style="border: none;"></iframe>
            """, 
            height=max_height
        )
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

# Key Takeaways and Implications
st.markdown("""
**Key Takeaways:**

- **Economic Health Score**: The current economic health score suggests a robust and stable economy with sustained growth momentum. However, continuous monitoring is crucial as the global economic landscape remains dynamic.
- **Debt-to-GDP Ratio**: While the Debt-to-GDP ratio is rising, it remains at manageable levels, suggesting that fiscal policy is under control. However, any significant rise in this ratio could signal potential risks for future fiscal stability and debt sustainability.
- **Revenue Trends**: The consistent growth in revenue is a positive sign, indicating healthy economic activity and strong fiscal management. This aligns with a stable outlook for the economy, suggesting that government revenue can support essential fiscal policies without significant debt accumulation.
- **Interest Coverage Ratio**: A favorable trend in the Interest Coverage Ratio signals that the economy is effectively managing its debt obligations. This implies that debt service is becoming more manageable, reducing the risk of fiscal strain.
- **Surplus/Deficit Position**: The improving surplus/deficit position reflects effective fiscal management and suggests that the government is successfully balancing expenditures and revenues. This may provide the necessary flexibility for future economic policy maneuvers without jeopardizing fiscal health.

**Implications for Decision-Making:**

- **Policy-makers**: Given the overall stability reflected in the dashboard, policymakers can prioritize long-term investments and infrastructure development, knowing that current fiscal health supports such initiatives. However, caution is needed as global uncertainties, such as geopolitical risks or market fluctuations, could affect these indicators.
- **Investors**: The combination of positive revenue trends and manageable debt levels presents a favorable environment for investments. Investors should feel confident about fiscal health in the short to medium term but should remain aware of the risks associated with increasing debt-to-GDP ratios.
- **General Implications**: The dashboard highlights a strong, sustainable fiscal environment, but it also flags the importance of keeping an eye on rising debt levels and global risks that could shift these positive trends. This data should inform decisions regarding long-term financial strategies, both for government and private sector planning.
""")
