import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Asset Class Behavior in Macroeconomic Context",
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

# Title for the page
st.title("Asset Class Behavior in Macroeconomic Context")
st.write("This page displays the behavior of different asset classes based on macroeconomic indicators.")

# Define the plot files, titles, and sizes
PLOT_FILES = [
    ("gdp_mom_regime.html", "GDP MOM Regime", 2400, 1000),
    ("gdp_regime_heatmap.html", "GDP Regime Heatmap", 2400, 1000),
    ("gdp_curr_regime_heatmap.html", "GDP Current Regime Heatmap", 2400, 500),
    ("inflation_YoY_regime.html", "Inflation YoY Regime", 2400, 1000),
    ("inflation_regime_heatmap.html", "Inflation Regime Heatmap", 2400, 1000),
    ("inflation_curr_regime_heatmap.html", "Inflation Current Regime Heatmap", 2400, 500),
    ("ir_regime.html", "Interest Rate Regime", 2400, 1000),
    ("ir_regime_heatmap.html", "Interest Rate Regime Heatmap", 2400, 1000),
    ("ir_curr_regime_heatmap.html", "Interest Rate Current Regime Heatmap", 2400, 500),
    ("asset_correlation_heatmap.html", "Asset Correlation Heatmap", 2400, 1000)
]

PLOT_DESCRIPTIONS = {
    "gdp_mom_regime.html": """
        In this visual, we can see a slight growing trend in GDP changes MoM. In recent years, we can see the 
        MoM changes becoming more volatile, possibly related to recent economic challenges. The momentum indicator 
        is still showcasing upward momentum.
    """,
    
    "gdp_regime_heatmap.html": """
        This heatmap showcases historical asset performance averages across different GDP regimes.
    """,
    
    "gdp_curr_regime_heatmap.html": """
        This heatmap showcases historical asset performance averages across the current GDP regime.
    """,
    
    "inflation_YoY_regime.html": """
        From the visual, we can see a slight growing trend in inflation levels. The momentum indicator is still showcasing upward momentum.
    """,
    
    "inflation_regime_heatmap.html": """
        This heatmap showcases historical asset performance averages across different inflation regimes.
    """,
    
    "inflation_curr_regime_heatmap.html": """
        This heatmap showcases historical asset performance averages across the current inflation regime.
    """,
    
    "ir_regime.html": """
        In this visual, we can see that in recent years, interest rate movements have seen a similar pattern to those seen
        back in the 2008 market crash. The momentum indicator is still showcasing upward momentum.
    """,
    
    "ir_regime_heatmap.html": """
        This heatmap showcases historical asset performance averages across different interest rate regimes.
    """,
    
    "ir_curr_regime_heatmap.html": """
        This heatmap showcases historical asset performance averages across the current interest rate regime.
    """,
    
    "asset_correlation_heatmap.html": """
        Correlation analysis across all major asset classes. The heatmap reveals both strong and weak relationships between different investment vehicles. 
        This analysis is necessary for portfolio construction and risk management decisions.
    """
}

# Additional analysis for specific relationships you mentioned:
RELATIONSHIP_DESCRIPTIONS = {
    "usa_gdp_sp500": """
        Analysis reveals a significant correlation between S&P 500 performance and U.S. GDP growth. 
        Historical data demonstrates that substantial GDP increases typically correspond with strong S&P 500 price appreciation, 
        highlighting the market's sensitivity to economic growth indicators.
    """,
    
    "usa_cpi_sp500": """
        A notable correlation exists between the S&P 500 and U.S. CPI movements. Sharp increases in the Consumer Price Index 
        have historically coincided with significant upward movements in the S&P 500, suggesting the market's capacity to act as an inflation hedge.
    """,
    
    "usa_ppi_sp500": """
        Analysis indicates minimal correlation between the Producer Price Index and S&P 500 performance. 
        This lack of correlation suggests that PPI movements may not be a reliable indicator for equity market direction.
    """,
    
    "usa_unemployment_sp500": """
        A correlation exists between unemployment rates and S&P 500 performance, notably with a lag effect. 
        This lagged relationship provides valuable secondary confirmation for market analysis and can serve as a supplementary indicator for market trends.
    """,
    
    "usa_interest_rate_sp500": """
        Evidence shows a strong correlation between interest rates and S&P 500 performance, with interest rates typically serving as a leading indicator. 
        This relationship provides valuable forward-looking insights for market analysis and can be particularly useful for strategic investment planning.
    """
}

# Path to the plots folder
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display the plots with specified sizes
for plot_file, plot_title, max_width, max_height in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        
        st.markdown(f"### {plot_title}")

        # Add the description if it exists
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
        
        # Embed the plot dynamically based on width and height
        html = f'''
            <div style="width: {max_width}px; height: {max_height}px; margin-bottom: 20px; border: 1px solid #ddd; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); overflow: hidden;">
                {html_content}
            </div>
        '''
        components.html(html, height=max_height)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

# Key Takeaways and Implications
st.markdown("""
**Key Takeaways:**

- **Implication**: The analysis above can be used in combination to anticipate the performance of assets given the various market regimes.    
- **Asset Correlation**: Understanding correlations between asset classes is crucial for portfolio construction, risk management, and optimization.

**Implications for Decision-Making:**
- Investors should closely monitor interest rates, GDP growth, and inflation trends as part of their strategic investment analysis process.
- Correlation studies between different asset classes can inform diversification strategies and optimal asset allocation.
""")
