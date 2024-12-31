import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Economic Health Dashboard",
    layout="wide"
)

# Apply custom CSS to remove left white line and zoom out
st.markdown(
    """
    <style>
        /* Adjust overall page zoom */
        body {
            zoom: 80%; /* Adjust this value as needed */
        }

        /* Streamlit container adjustments */
        .main .block-container {
            max-width: 2500px; /* Wider page container */
            padding-left: 0rem;  /* Remove left padding */
            padding-right: 2rem; /* Maintain right padding */
            margin-left: 0px;    /* Remove left margin */
        }

        /* Remove default margin and padding around body and page */
        .css-18e3th9 {
            margin: 0;  /* Remove margin */
            padding: 0; /* Remove padding */
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("📊 Economic Health Dashboard")
st.write("This page displays key economic health indicators through interactive HTML plots.")

# Define plot order and titles
PLOT_FILES = [
    ("Econ_Health_Score.html", "Economic Health Score"),
    ("DGDP_Ratio.html", "Debt-to-GDP Ratio"),
    ("usa_revenue.html", "USA Revenue"),
    ("Interest_Cov_Ratio.html", "Interest Coverage Ratio"),
    ("usa_sur_def.html", "USA Surplus/Deficit")
]

# Path to the plots folder
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display the plots in order
for plot_file, plot_title in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        
        st.markdown(f"### {plot_title}")
        
        # Embed plot without scrolling
        html = f'''
            <div style="
                width: 2200px;
                height: 1000px;
            ">
                {html_content}
            </div>
        '''
        components.html(html, height=1000)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")
