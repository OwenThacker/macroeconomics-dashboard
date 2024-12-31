import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="SP500 Analysis",
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
            color: #8BC34A;  /
            font-size: 2.0 em; /* Largest text for the main title */
            font-weight: bold;
            margin-bottom: 20px;
        }

        /* Section title styling */
        .section-title {
            font-size: 1.6m; /* Clear and bold subtitle */
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

# Define plot descriptions
PLOT_DESCRIPTIONS = {
    "sp500_gdp_mom.html": """
        The analysis demonstrates a strong correlation between the S&P 500 performance and U.S. GDP growth.
        Historical data reveals that movements in either often provide a directional bias for the other, 
        making GDP a useful indicator for market positioning.
    """,
    
    "sp500_cpi_mom.html": """
        The correlation between the S&P 500 and CPI shows a general upward trend, though the relationship is looser.
        This suggests that while there is some level of alignment, other factors should also be considered in analysis.
    """,
    
    "sp500_ppi_mom.html": """
        A more random and loosely correlated movement is observed here. While PPI impacts inflation trends, 
        its relationship with the S&P 500 appears inconsistent and should be interpreted with caution.
    """,
    
    "sp500_unemp_mom.html": """
        Visually, the line plots provide no significant correlation between unemployment figures and the 
        S&P 500 performance in this analysis.
        However, the momentum indicator is a good confirmation indicator.
    """,
    
    "sp500_ir_mom.html": """
        A strong correlation is evident between interest rates and S&P 500 performance, with interest rates often acting 
        as a leading indicator. This relationship can be leveraged to anticipate market movements, offering valuable 
        forward-looking insights for strategic investment planning.
    """
}

# Title for the page
st.title("SP500 Analysis")
st.write("This page presents an analysis of the S&P 500 index with respect to key economic indicators. "
         "The goal is to explore the relationships between macroeconomic data and market performance, offering insights "
         "that may inform strategic investment decisions.")

# Define the plot files, titles, and sizes
PLOT_FILES = [
    ("sp500_gdp_mom.html", "SP500 GDP MOM Analysis", 2200, 1000),
    ("sp500_cpi_mom.html", "SP500 CPI MOM Analysis", 2200, 1000),
    ("sp500_ppi_mom.html", "SP500 PPI MOM Analysis", 2200, 1000),
    ("sp500_unemp_mom.html", "SP500 Unemployment MOM Analysis", 2200, 1000),
    ("sp500_ir_mom.html", "SP500 Interest Rate MOM Analysis", 2200, 1000)
]

# Path to the plots folder
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display the plots with specified sizes
for plot_file, plot_title, width, height in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        
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
        
        # Embed the plot dynamically based on width and height
        html = f'''
            <div style="
                width: {width}px;
                height: {height}px;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
                overflow: hidden;
            ">
                {html_content}
            </div>
        '''
        components.html(html, height=height)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

# Overview and Implications
st.markdown("""
**Key Takeaways:**

- **Interest Rates**: Strongly correlated with the S&P 500, serving as a potential leading indicator for market performance. 
- **GDP Growth**: A significant correlation indicates that economic growth trends often mirror S&P 500 performance, providing directional bias for market positioning.
- **Inflation (CPI and PPI)**: While these metrics show some correlation, the relationship is less defined, suggesting that inflationary trends might influence long term market behavior, but not always predictably.
- **Unemployment**: Little correlation observed with market performance in the short term, but long-term trends may offer additional conirmation.

**Implications for Decision-Making:**
- Investors can leverage these relationships to better anticipate market shifts and refine their strategies. 
- Interest rates, GDP growth, and inflation trends are especially useful for identifying potential changes in market direction.
- However, caution should be exercised with metrics like unemployment, which show less immediate impact on market movements.
""")
