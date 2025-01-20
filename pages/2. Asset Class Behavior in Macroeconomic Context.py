import streamlit as st
import streamlit.components.v1 as components
import os
import base64
from datetime import datetime

# Configure Streamlit page
st.set_page_config(
    page_title="Economic Health Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to encode images to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

# Get base64-encoded image
image_path = os.path.join(os.getcwd(), 'plots', 'sp500_gdp.png')
image_base64 = image_to_base64(image_path)

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


# Function to load HTML plots with consistent styling
def load_html_plot(plot_name, height=None):
    try:
        plot_path = os.path.join("plots", f"{plot_name}.html")
        with open(plot_path, "r", encoding="utf-8") as f:
            plot_html = f.read()

            # Set default or provided height
            if not height:
                if "PCA" in plot_name:
                    height = 2200
                elif any(keyword in plot_name for keyword in ["gdp", "inf", "int", "heatmap"]):
                    height = 1600
                else:
                    height = 3000

            # Styled HTML wrapper for consistency with minimal spacing
            styled_html = f"""
            <div style="width: 100%; max-width: 2400px; margin: 0 auto; 
                        border: 1px solid #E0E0E0; border-radius: 12px; 
                        padding: 1rem 0.5rem 0rem; background-color: #FFFFFF;">
                {plot_html}
            </div>
            """
            components.html(styled_html, height=height)
    except FileNotFoundError:
        st.error(f"Plot '{plot_name}' not found.")
    except Exception as e:
        st.error(f"Error loading plot: {e}")


# Analysis Categories with User-Friendly Titles
analysis_categories = {
    "Heatmap Analysis": [
        ("gdp_regime_heatmap", "Heatmap of Asset Performance in Different GDP Regimes", "curr_reg_gdp"),
        ("inflation_regime_heatmap", "Heatmap of Asset Performance in Different Inflation Regimes", "curr_reg_inf"),
        ("int_regime_heatmap", "Heatmap of Asset Performance in Different Interest Rate Regimes", "curr_reg_int")
    ],
    "Macro Regime Momentum Analysis": [
        ("gdp_mom_regime", "GDP Month-over-Month Growth Regime", None),
        ("inflation_YoY_regime", "Inflation Year-over-Year Growth Regime", None),
        ("ir_regime", "Interest Rate Regime", None)
    ]
}

# Main Content
st.markdown("""
    <div style="padding: 1rem 0 2rem 0;">
        <h1 style="color: #2E7D32; font-size: 2.5rem; font-weight: 700; margin-bottom: 0.5rem;">Economic Health Dashboard</h1>
        <p style="color: #666666; font-size: 1.2rem; max-width: 800px;">
            Explore interactive visualizations of economic trends and asset behavior across various market conditions.
        </p>
    </div>
""", unsafe_allow_html=True)

# Category and Plot Selection
selected_category = st.selectbox("Select Analysis Category", options=list(analysis_categories.keys()))
plots_in_category = analysis_categories[selected_category]
selected_plot = st.selectbox(
    "Select Analysis View",
    plots_in_category,
    format_func=lambda x: x[1]  # Display user-friendly title
)

# Check for Secondary Plot (e.g., Current Regime Analysis)
secondary_plot = selected_plot[2]  # Access the corresponding current regime plot, if any
if secondary_plot:
    st.markdown("""
        <div style="color: #2E7D32; font-size: 1.5rem; font-weight: 700; margin-bottom: 0rem;">
            Current Market Regime
        </div>
    """, unsafe_allow_html=True)
    load_html_plot(secondary_plot, height=300)  # Current regime plot displayed above

# Display Main Heatmap Plot
load_html_plot(selected_plot[0])  # Load primary plot

# Footer
st.markdown(f"""
    <div style="text-align: center; padding: 1rem; background-color: #F8FAF8; margin-top: 2rem; border-top: 1px solid #E0E0E0;">
        Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}
    </div>
""", unsafe_allow_html=True)