import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Yield Curve Analysis",
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

# Title for the page
st.title("Yield Curve Analysis")
st.write("Explore the key trends and forecasts derived from various yield curve models, including steepness analysis and CIR projections.")

# Plot descriptions
PLOT_DESCRIPTIONS = {
    "Yield_Curve_with_Steepness.html": "Shows the overall yield curve along with its steepness. Steep curves often point to expectations of economic growth, while flatter curves could signal economic slowdown or market uncertainty.",
    "yield_steepness.html": "A focused look at yield curve steepness, which is helps for understanding the difference in returns between short and long-term bonds over time. Steeper curves typically suggests growth optimism, while flatter curves often signals economic stagnation or uncertainty.",
    "CIR_Model.html": "The Cox-Ingersoll-Ross model. The model assumes rates tend to revert to a long-term mean.",
    "CIR_Model_MonteCarlo_Hist.html": "Monte Carlo simulation of the CIR model, predicting the potential paths interest rates might take over the next month. Forecasted interest rate of 4.3295, with standard deviation 0.0320",
    "CIR_Model_Yield.html": "Zero coupon bond yield curve, using the CIR model forecasted interest rate (Next months expected yield curve)"
}

# Define the plot files, titles, and sizes
PLOT_FILES = [
    ("Yield_Curve_with_Steepness.html", "Yield Curve with Steepness", 2400, 1000),
    ("yield_steepness.html", "Yield Steepness", 2400, 800),
    ("CIR_Model.html", "Cox-Ingersoll-Ross (CIR) Model", 2400, 500),
    ("CIR_Model_MonteCarlo_Hist.html", "CIR Model Monte Carlo Simulation (Next Month Forecasted)", 2200, 500),
    ("CIR_Model_Yield.html", "CIR Model Yield Curve", 2400, 500)
]

# Path to the plots folder
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display the plots with specified sizes and add descriptions
for plot_file, plot_title, max_width, max_height in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        
        st.markdown(f"### {plot_title}")
        
        # Display the plot description
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
        
        # Embed the plot with auto-scaling for oversized plots
        html = f'''
            <div style="max-width: {max_width}px; max-height: {max_height}px; width: 100%; height: 100%; margin-bottom: 20px;">
                <div style="display: flex; justify-content: center; align-items: center;">
                    <div style="width: 100%; height: 100%; overflow: hidden;">
                        {html_content}
                    </div>
                </div>
            </div>
        '''
        components.html(html, height=max_height)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")

# Key Takeaways and Implications
st.markdown("""
### Key Takeaways:

- **Yield Curve with Steepness**: A steeper yield curve indicates positive expectations for economic growth and inflation, suggesting that investors are anticipating higher interest rates in the future. A flatter curve can signal economic slowdown or market uncertainty.
- **Yield Steepness**: Monitoring steepness helps investors understand the relative health of the economy. A rapid change in steepness can indicate shifting expectations for monetary policy, economic growth, or inflation.
- **Cox-Ingersoll-Ross (CIR) Model**: The CIR model shows how interest rates evolve, allowing us to anticipate the mean-reverting nature of short-term rates. The model is particularly useful for understanding the impact of current rates on future market conditions.
- **CIR Model Monte Carlo Simulation**: The Monte Carlo simulation provides a range of potential interest rate paths, helping to quantify risk and identify the most probably outcome.
- **CIR Model Yield Curve**: This plot helps to assess the potential furture bond market, aiding decision makers.

### Implications for Decision-Making:

- **For Policymakers**: The yield curve steepness and CIR model simulations give a clear indication of where the economy might be heading. A steep yield curve may prompt central banks to consider tightening, while a flat curve may signal the need for rate cuts to stimulate growth.
- **For Investors**: Investors can use this analysis to adjust their portfolios, especially in fixed income. Steep curves may favor riskier, longer-duration assets, while flatter curves may suggest shifting towards shorter-duration or defensive positions.
- **For Analysts**: Combining yield curve analysis with the CIR model gives a comprehensive view of the market’s expectations. Analysts can use this to forecast future rate movements and anticipate potential market shifts.
""")
