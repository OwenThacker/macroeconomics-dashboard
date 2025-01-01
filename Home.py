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
    "Your input is essential in making this platform better. Please share your thoughts by answering the following questions:"
)
st.markdown(
    """
    - Did this platform provide valuable insights into macroeconomic trends?
    - How intuitive and user-friendly did you find the interface?
    - Were the visualizations helpful in understanding the data?
    - Is there any additional functionality or feature you would like to see?
    - Do you feel that the platform can assist in your decision-making process?
    - Could you see yourself using this platform regularly? Is it something I should keep working on, keeping updated, and improving?
    - Is this platform something you would pay for? If not, what would make you consider it as a paid service?
    """
)
st.markdown("</div>", unsafe_allow_html=True)

# Optional Footer or Contact Information with Feedback Request
st.markdown("<h3 class='section-title'>Contact & Support</h3>", unsafe_allow_html=True)
st.write(
    "For inquiries or feedback, please contact me at: [Owenthacker13@hotmail.com](mailto:Owenthacker13@hotmail.com)."
)
