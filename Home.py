import streamlit as st

# Apply custom CSS for light theme
st.markdown(
    """
    <style>
        body {
            background-color: #ffffff;  /* White background */
            color: #000000;  /* Black text color */
        }

        .title {
            color: #1f77b4;  /* Blue color for the title */
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
    </style>
    """,
    unsafe_allow_html=True
)

# Page Title
st.markdown("<h1 class='title'>Welcome to the Economic Health Dashboard</h1>", unsafe_allow_html=True)

# Introduction Section
st.markdown("<h2 class='section-title'>What is this platform?</h2>", unsafe_allow_html=True)
st.write(
    "The Economic Health Dashboard is a comprehensive platform designed to provide in-depth analysis of macroeconomic indicators and asset class behaviors."
    " The platform utilizes advanced financial models, interactive visualizations, and real-time data to offer valuable insights into economic conditions."
    " Whether you are an investor, financial analyst, or researcher, this platform helps you understand the global economic landscape and make data-driven decisions."
)

# Why Section
st.markdown("<h2 class='section-title'>Why does it exist?</h2>", unsafe_allow_html=True)
st.write(
    "In today's dynamic and fast-paced global economy, understanding macroeconomic trends and their impact on asset classes is crucial."
    " This platform exists to fill the gap in easily accessible, interactive, and actionable macroeconomic data analysis."
    " By integrating diverse datasets and financial models, we aim to provide a comprehensive tool for identifying investment opportunities, managing risks, and making informed decisions."
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

# Optional Footer or Contact Information
st.markdown("<h3 class='section-title'>Contact & Support</h3>", unsafe_allow_html=True)
st.write(
    "For inquiries or feedback, please contact us at: [your-email@example.com](mailto:your-email@example.com). We are here to help you make the most out of the platform."
)