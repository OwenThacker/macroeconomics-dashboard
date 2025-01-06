import streamlit as st
import streamlit.components.v1 as components
import os
import base64

# Apply custom CSS for light theme
st.markdown(
    """
    <style>
        body {
            background-color: #ffffff;  /* White background */
            color: #000000;  /* Black text color */
        }

        .title {
            color: #8BC34A;  /* Blue color for the title */
            font-weight: bold;
        }

        .section-title {
            color: #333333;  /* Dark grey color for section titles */
            font-weight: bold;
        }

        .section-content {
            font-size: 18px;
            line-height: 1.6;
        }

        .highlight {
            background-color: #f9f9f9; /* Light background for important text */
            padding: 5px;
            border-radius: 4px;
        }

        .footer {
            border-top: 1px solid #e0e0e0;
            padding-top: 15px;
            margin-top: 30px;
            text-align: center;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<h1 class='title'>Welcome to the Economic Health Dashboard</h1>", unsafe_allow_html=True)


# Plot descriptions
PLOT_DESCRIPTIONS = {
    "Econ_Health_Score.html": "The Economic Health Heatmap provides a overview of the economy's current state"
}

# Page title
st.title("Economic Health Dashboard")

# Plot details with individual dimensions (width and height)
PLOT_FILES = [
    ("Econ_Health_Score.html", "Economic Health Score", "100%", 1000),
]

PLOTS_PATH = os.path.join(os.path.dirname(__file__), "plots")

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

# Introduction Section
st.markdown("<h2 class='section-title'>What is this platform?</h2>", unsafe_allow_html=True)
st.write(
    "The Economic Health Dashboard is a comprehensive platform designed to provide in-depth analysis of macroeconomic indicators and asset class behaviors."
    " The platform utilizes advanced financial models, interactive visualizations, and real-time data to offer insights into economic conditions."
    " Whether you are an investor, financial analyst, or researcher, this platform helps you understand the global economic landscape and make data-driven decisions."
)

# Why Section
st.markdown("<h2 class='section-title'>Why does it exist?</h2>", unsafe_allow_html=True)
st.write(
    "In today's dynamic and fast-paced global economy, understanding macroeconomic trends and their impact on asset classes is crucial."
    " This platform exists to fill the gap in easily accessible, interactive, and actionable macroeconomic data analysis."
    " By integrating diverse datasets and financial models, we aim to provide a comprehensive tool for help YOU make informed decisions."
)

# Who Section
st.markdown("<h2 class='section-title'>Who is it for?</h2>", unsafe_allow_html=True)
st.write(
    "This platform is primarily designed for professionals in the finance and investment industries. However, it can be useful for anyone interested in understanding the economic forces that drive global markets."
)
st.markdown(
    """
    **Target Audience:**
    - **Investment Funds & Hedge Funds:** For analyzing macroeconomic indicators and their effects on asset classes.
    - **Financial Analysts & Researchers:** To gain insights into the economic landscape for decision-making and forecasting.
    - **Real Estate & Property Developers:** To assess the impact of macroeconomic conditions on the real estate market.
    - **Policy Makers & Economists:** To monitor economic health and assess policy impacts.
    """
)

# Call to Action Section
st.markdown("<h2 class='section-title'>Start Exploring!</h2>", unsafe_allow_html=True)
st.write(
    "Explore the different sections of the platform to understand the global economic context, assess asset class behavior, and dive deep into macroeconomic trends."
    " Select a dashboard from the sidebar to start analyzing the data."
)

# Feedback Section (Updated with final question)
st.markdown("<div class='footer'>", unsafe_allow_html=True)
st.markdown("<h4 class='section-title'>We value your feedback</h4>", unsafe_allow_html=True)
st.write(
    "Your input is essential in making this platform better. Please share your thoughts by answering the feedback form in the feeback section"
)

