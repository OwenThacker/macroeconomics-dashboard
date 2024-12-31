import streamlit as st
import streamlit.components.v1 as components
import os

# Page configuration
st.set_page_config(
    page_title="Yield Curve Analysis",
    layout="wide"
)

# Apply custom CSS for light theme
st.markdown(
    """
    <style>
        body {
            background-color: #ffffff;  /* White background */
            color: #000000;  /* Black text color */
            zoom: 80%;  /* Adjust zoom level */
        }

        /* Streamlit container adjustments */
        .main .block-container {
            max-width: 2500px;  /* Wider page container */
            padding-left: 0rem;  /* Remove left padding */
            padding-right: 2rem;  /* Maintain right padding */
            margin-left: 0px;  /* Remove left margin */
        }

        /* Customize header font color */
        h1, h2, h3, h4, h5, h6 {
            color: #333333;  /* Dark grey headers */
        }

        /* Customize Streamlit button color */
        .stButton>button {
            background-color: #1f77b4;  /* Blue button color */
            color: white;  /* White text color */
        }

        /* Styling for interactive elements (select boxes, sliders, etc.) */
        .stSelectbox, .stSlider, .stTextInput {
            background-color: #f9f9f9;  /* Light background for inputs */
        }

        /* Remove default margin and padding around body */
        .css-18e3th9 {
            margin: 0;  /* Remove margin */
            padding: 0;  /* Remove padding */
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title for the page
st.title("Yield Curve Analysis")
st.write("This page presents various yield curve analyses, including the CIR model and its Monte Carlo simulation.")

# Define the plot files and titles
PLOT_FILES = [
    ("Yield_Curve_with_Steepness.html", "Yield Curve with Steepness"),
    ("yield_steepness.html", "Yield Steepness"),
    ("CIR_Model.html", "Cox-Ingersoll-Ross (CIR) Model"),
    ("CIR_Model_MonteCarlo_Hist.html", "CIR Model Monte Carlo Simulation (Historical)"),
    ("CIR_Model_Yield.html", "CIR Model Yield Curve")
]

# Path to the plots folder
PLOTS_PATH = os.path.join(os.path.dirname(__file__), "..", "plots")

# Display the plots in the specified order
for plot_file, plot_title in PLOT_FILES:
    plot_path = os.path.join(PLOTS_PATH, plot_file)
    
    if os.path.exists(plot_path):
        with open(plot_path, "rb") as f:
            html_content = f.read().decode(errors="ignore")
        
        st.markdown(f"### {plot_title}")
        
        # Embed the plot without scrolling
        html = f'''
            <div style="
                width: 2200px;
                height: 1000px;
                margin-bottom: 20px;
                border: 1px solid #ddd;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.1);
            ">
                {html_content}
            </div>
        '''
        components.html(html, height=1000)
    else:
        st.error(f"Plot file '{plot_file}' not found in {PLOTS_PATH}")
