import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime
import os
import base64
from PIL import Image

# Configure Streamlit page
st.set_page_config(
    page_title="Alterra | Economic Overview Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paths to the original and new images
original_image_path = os.path.join(os.getcwd(), 'plots', 'sp500_gdp.png')
new_image_path = os.path.join(os.getcwd(), 'plots', 'wheat_field.jpg')

# Open both images
original_image = Image.open(original_image_path)
new_image = Image.open(new_image_path)

# Resize the new image to match the dimensions of the original
new_image_resized = new_image.resize(original_image.size, Image.Resampling.LANCZOS)

# Save the resized image
new_image_resized_path = os.path.join(os.getcwd(), 'plots', 'Mining_resized.jpg')
new_image_resized.save(new_image_resized_path)

# Use the resized image for the dashboard
image_path = new_image_resized_path

# Function to encode image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

# Get the base64 encoded image
image_base64 = image_to_base64(image_path)

# Update the font sizes by increasing them by 2 levels
st.markdown(f"""
    <style>
        /* Scale the entire page but keep the sidebar unaffected */
        .stApp > div {{
            transform: scale(0.67);
            transform-origin: top center;
            width: 200%;
            height: 150%;
            margin-left: -33%;
        }}

        /* Sidebar Styles - Keep sidebar text unchanged */
        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
        }}

        /* Main content area (excluding sidebar) */
        .main {{
            background-color: #FFFFFF;
            font-size: 1.2rem;  /* Increased font size by 2 levels */
        }}

        /* Hero Section Styles - Move the background image and ensure it fills the screen */
        .hero-container {{
            position: relative;
            padding: 11rem 2rem; /* Adjusted padding to push it down */
            text-align: center;
            margin: 0 -4rem 1rem -4rem; /* Adjusted margin */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Full screen height */
            color: white;
            background-image: linear-gradient(
                rgba(0, 0, 0, 0.5),
                rgba(0, 0, 0, 0.5)
            ), url("{image_base64}");
            background-size: cover; /* Ensure image covers the entire container */
            background-position: center top; /* Ensure background starts from the top and stays centered */
            background-repeat: no-repeat;
            position: relative;
            overflow: hidden;
        }}

        /* Add a semi-transparent overlay */
        .hero-container::before {{
            content: '';
            position: absolute;
            top: 0rem; /* Align overlay with the background position */
            left: 0;
            right: 0;
            bottom: 0;
            background: linear-gradient(
                180deg,
                rgba(255, 255, 255, 0.95) 0%,
                rgba(255, 255, 255, 0.8) 30%,
                rgba(255, 255, 255, 0.6) 60%,
                rgba(255, 255, 255, 0.4) 100%
            );
            z-index: 1;
        }}

        /* Hero Title - Move the title down */
        .company-title {{
            font-size: 150px !important;  /* Explicitly set title font size */
            font-weight: 700;
            color: #2E7D32;
            letter-spacing: -1px;
            margin-bottom: 1rem;
            z-index: 2;
            margin-top: -9rem; /* Adjusted margin to move the title down */
            text-shadow: 2px 2px 4px rgba(255, 255, 255, 0.5);
            position: relative;
        }}

        /* Subtitle - Adjusted size and margin */
        .company-subtitle {{
            font-size: 30px !important;  /* Explicitly set subtitle font size */
            color: #1B5E20;
            max-width: 800px;
            margin: 0 auto;
            z-index: 2;
            position: relative;
            text-shadow: 1px 1px 2px rgba(255, 255, 255, 0.5);
            background: rgba(255, 255, 255, 0.3);
            padding: 1rem;
            border-radius: 8px;
            backdrop-filter: blur(5px);
        }}

        /* Market Insight Cards (Market Pulse Cards) */
        .insight-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
            padding: 2rem 0;
            margin-top: -25rem;
        }}

        .insight-card {{
            background: #FFFFFF;
            border-radius: 12px;
            padding: 0.5rem;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }}

        [data-testid="stSidebar"] .insight-card {{
            width: calc(150%); /* Full width minus padding */
            box-sizing: border-box;
            margin: 0.5rem 1rem;
            margin-left: 0.2rem;
        }}

        .insight-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }}

        .insight-title {{
            font-size: 1.6rem;  /* Increased insight title font size */
            color: #2E7D32;
            font-weight: 600;
        }}

        .insight-content {{
            font-size: 1.4rem;  /* Increased insight content font size */
            color: #262626;
            margin-top: 0.5rem;
        }}

        .insight-footer {{
            font-size: 1.1rem;  /* Increased footer font size */
            color: #90A4AE;
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }}

        .insight-impact {{
            color: #2E7D32;
            font-weight: 600;
        }}

        /* About Section */
        .about-section {{
            background: #F8F9FA;
            border-radius: 16px;
            padding: 4rem 2rem;
            margin: 2rem 0;
        }}

        .feature-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }}

        .feature-card {{
            background: #FFFFFF;
            border-radius: 12px;
            padding: 1.5rem;
            text-align: center;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
        }}

        .feature-card:hover {{
            border-color: #2E7D32;
        }}

        /* Upsize Text for Main Content Only */
        body, .stApp, .main, .insight-title, .insight-content, .insight-footer, .company-title, .company-subtitle {{
            font-size: 1.2rem;  /* Increase font size of main content */
        }}
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
    st.markdown("### Top New Market Insights", unsafe_allow_html=True)
    insights = [
        {
            "title": "Global Tech Sell Off",
            "content": "Investor concern with the new release of China's DeepSeek model. Nvidia falls 14% in premarket trading",
            "trend": "↘️ Falling",  # Changed to diagonal downward arrow
            "impact": "High"
        },
        {
            "title": "Fed Holding Rates",
            "content": "Fed rate cut 'probably not until the second half of the year' says economist Odeta Kushi of First American",
            "trend": "→ Stable",
            "impact": "High"
        },
        {
            "title": "Highest interest rates in Japan in 17 Years",
            "content": "BoJ raises short-term policy rate 25 bps to 0.5% from 0.25%, causing a jump in the Yen",
            "trend": "↗️ Growing",
            "impact": "High"
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

# Insights to be displayed across multiple cards
insights = [
    {
        "title": "China's Economic Struggles",
        "content": (
            "China has dramatically increased its private sector leverage over the last decade, which is now causing problems, particularly due to a troubled real estate market."
        ),
        "trend": "↗️ Rising",
        "impact": "High"
    },
    {
        "title": "Housing Market Crisis in Canada, Sweden, and Switzerland",
        "content": (
            "Canada, Sweden, and Switzerland heavily rely on their housing markets and high household debt. With interest rates rising in 2022-2023 following the Fed's actions, these economies are now feeling the effects. "
            "Variable rate mortgages and refinancing cliffs add to the strain."
        ),
        "trend": "↗️ Growing",
        "impact": "Medium"
    },
    {
        "title": "Fears of Inflation in 2025",
        "content": (
            "For 2025, inflation remains a significant concern. The steepening of the yield curve, driven by fewer (or no) rate cuts than expected, and the ongoing increase in the term premium are causes for worry. "
            "If the economy accelerates, inflation might resurge unexpectedly. "
            "The Federal Reserve is walking back from further rate cuts until the disinflation trend resumes."
        ),
        "trend": "↗️ Growing",
        "impact": "High"
    },
    {
        "title": "Fed's Policy and Inflation Control",
        "content": (
            "As for the Federal Reserve, it is right to walk back from further rate cuts until the disinflation trend of 2023 resumes. "
            "The downside momentum for short-term rates has ended, and the Fed is in the right place at 4.25-50%. Further cuts are not justified until inflation approaches its target."
        ),
        "trend": "→ Stable",
        "impact": "Moderate"
    },
    {
        "title": "Recession Probability Rising",
        "content": (
            "Recession probabilities are trending upwards, with the current probability at 33.14% and expected to rise to 68% in the next 12 months."
        ),
        "trend": "↗️ Rising",
        "impact": "High"
    }
]

# Hero Section with Reduced Opacity Background Image
st.markdown("""
    <div class="hero-container">
        <div class="company-title">ALTERRA</div>
        <div class="company-subtitle">
            Transforming Economic Intelligence into Strategic Advantage
        </div>
    </div>
""", unsafe_allow_html=True)


# Market Insights Section (with reduced margin and styled like navigation cards)
st.markdown("""
    <div style="padding: 0rem 0;"> <!-- Adjust padding above the header -->
    <!-- Market Insights Header -->
    <h2 class="market-insights-header" style="color: #2E7D32; font-size: 2rem; margin-bottom: 0.5rem; margin-top: 0rem;">
        Top 5 Market Insights This Quarter
    </h2>
    <!-- Insight Cards Grid -->
    <div class="insight-grid" style="margin-top: -2rem;"> <!-- Reset margin-top of the cards -->
        <!-- Insight 1 -->
        <div class="insight-card">
            <div class="insight-title">China's Economic Struggles</div>
            <div class="insight-content">
                China has dramatically increased its private sector leverage over the last decade, which is now causing problems, particularly due to a troubled real estate market.
            </div>
            <div class="insight-footer">
                <div>↗️ Rising</div>
                <div class="insight-impact">High</div>
            </div>
        </div>
        <!-- Insight 2 -->
        <div class="insight-card">
            <div class="insight-title">Housing Market Crisis in Canada, Sweden, and Switzerland</div>
            <div class="insight-content">
                Canada, Sweden, and Switzerland heavily rely on their housing markets and high household debt. With interest rates rising in 2022-2023 following the Fed's actions, these economies are now feeling the effects. Variable rate mortgages and refinancing cliffs add to the strain.
            </div>
            <div class="insight-footer">
                <div>↗️ Growing</div>
                <div class="insight-impact">Moderate</div>
            </div>
        </div>
        <!-- Insight 3 -->
        <div class="insight-card">
            <div class="insight-title">Fears of Inflation in 2025</div>
            <div class="insight-content">
                For 2025, inflation remains a significant concern. The steepening of the yield curve, driven by fewer (or no) rate cuts than expected, and the ongoing increase in the term premium are causes for worry. If the economy accelerates, inflation might resurge unexpectedly.
                The Federal Reserve is walking back from further rate cuts until the disinflation trend resumes.
            </div>
            <div class="insight-footer">
                <div>↗️ Growing</div>
                <div class="insight-impact">High</div>
            </div>
        </div>
        <!-- Insight 4 -->
        <div class="insight-card">
            <div class="insight-title">Fed's Policy and Inflation Control</div>
            <div class="insight-content">
                As for the Federal Reserve, it is right to walk back from further rate cuts until the disinflation trend of 2023 resumes. The downside momentum for short-term rates has ended, and the Fed is in the right place at 4.25-50%. Further cuts are not justified until inflation approaches its target.
            </div>
            <div class="insight-footer">
                <div>→ Stable</div>
                <div class="insight-impact">Moderate</div>
            </div>
        </div>
        <!-- Insight 5 -->
        <div class="insight-card">
            <div class="insight-title">Recession Probability Rising</div>
            <div class="insight-content">
                Recession probabilities are trending upwards, with the current probability at 33.14% and expected to rise to 68% in the next 12 months.
            </div>
            <div class="insight-footer">
                <div>↗️ Rising</div>
                <div class="insight-impact">High</div>
            </div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# Conclusion based on insights
st.markdown("""
    <div class="insight-card">
        <div class="insight-title">Conclusion</div>
        <div class="insight-content">
            The global economic outlook for 2025 is filled with potential risks. Key economies such as China, Canada, Sweden, and Switzerland are facing considerable challenges, particularly in the housing markets, which could lead to broader financial instability. 
            At the same time, inflation remains a concern, with fears of a resurgence in prices despite the Fed's recent policy decisions. 
            The increased probability of a recession, along with the ongoing inflationary pressures, suggests that the economy may face tough times ahead. As we continue to monitor the situation, businesses and investors should brace for potential market volatility.
        </div>
    </div>
""", unsafe_allow_html=True)

import streamlit as st
from PIL import Image
import base64
import os

# Function to encode an image to base64
def image_to_base64(image):
    with open(image, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

# Paths to the images
oil_digger_path = os.path.join(os.getcwd(), 'plots', 'oil_digger.jpg')
wheat_field_path = os.path.join(os.getcwd(), 'plots', 'wheat_field.jpg')
Mining_path = os.path.join(os.getcwd(), 'plots', 'Mining.jpg')

# Check if the image files exist
if not os.path.exists(oil_digger_path) or not os.path.exists(wheat_field_path):
    st.error("One or more image files are missing.")
else:
    # Convert images to base64
    oil_digger_base64 = image_to_base64(oil_digger_path)
    wheat_field_base64 = image_to_base64(wheat_field_path)
    Mining_base64 = image_to_base64(Mining_path)

    # Custom CSS for styling the About section
st.markdown(f"""
    <style>
        /* About Section Container */
        .about-container {{
            background: linear-gradient(rgba(255, 255, 255, 0.9), rgba(255, 255, 255, 0.9)), url("{Mining_base64}");
            background-size: cover;
            background-position: center;
            padding: 4rem 2rem;
            color: black;
            border-radius: 16px;
            margin-top: 3rem;
            position: relative;
        }}

        /* Title styling */
        .about-title {{
            font-size: 5rem; /* Bigger font size */
            font-weight: 700; /* Keep bold style */
            color: #2E7D32; /* Green color */
            text-align: center; /* Center-align the text */
            position: absolute; /* Allow the title to overlap the container */
            top: -9rem; /* Move the title above the container */
            left: 5%; /* Center the title horizontally */
        
            z-index: 10; /* Ensure the title is above other elements */
            padding: 0.5rem 1rem; /* Optional: Padding for the background */
            border-radius: 12px; /* Optional: Rounded corners for background */
        }}

        /* Content Grid Layout */
        .content-grid {{
            display: grid;
            grid-template-columns: 800px 1200px;  /* Fixed widths for 2400px container */
            gap: 4rem;  /* Increased gap */
            margin: 0 auto;
            max-width: 2400px;
            align-items: start;
            padding: 0 4rem;  /* Increased padding */
        }}

        /* Text Container */
        .text-container {{
            background: rgba(255, 255, 255, 0.95);
            padding: 2.5rem;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            width: 800px;  /* Fixed width */
        }}

        /* Description Styling */
        .about-description {{
            font-size: 1.3rem !important;  /* Increased font size */
            color: black;
            text-align: left;
            line-height: 1.8;
            margin-bottom: 2rem;  /* Increased spacing between paragraphs */
            margin-left: -20rem;
        }}

        .about-description:last-child {{
            margin-bottom: 0;
        }}

        /* Image Collage Styling */
        .image-collage {{
               display: grid;
                grid-template-columns: repeat(2, 1fr);
                grid-template-rows: repeat(2, 300px);  /* Fixed height rows */
                gap: 2rem;
                width: 1200px;  /* Fixed width */
        }}

        .image-1 {{
            grid-column: 1;
            grid-row: 1;
            width: 100%;
            height: 100%;
        }}

        .image-2 {{
            grid-column: 2;
            grid-row: 1 / span 2;  /* Spans both rows */
            width: 100%;
            height: 100%;
        }}

        .image-3 {{
            grid-column: 1;
            grid-row: 2;
            width: 100%;
            height: 100%;
        }}

        .collage-image {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 12px;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s ease;
        }}

        .collage-image:hover {{
            transform: scale(1.02);
        }}

        /* Closing Remarks */
        .closing-remarks {{
            font-size: 1.3rem !important;
            color: black;
            text-align: left;
            max-width: 2400px;
            margin: 2rem auto 0 auto;
            padding: 2.5rem 4rem;  /* Increased padding */
            background: rgba(255, 255, 255, 0.95);
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }}
    </style>
""", unsafe_allow_html=True)

# Main container for About Section
st.markdown('<div class="about-container">', unsafe_allow_html=True)

# Title
st.markdown('<div class="about-title">About Alterra</div>', unsafe_allow_html=True)

# Content Grid with Text and Image Collage
st.markdown(f"""
    <div class="content-grid">
        <div class="text-container">
            <p class="about-description">
                Alterra is revolutionizing the way organizations and investors access and utilize economic intelligence.
                In today's fast-paced and interconnected global markets, staying ahead requires more than just data—it demands insights.
                Our mission is to bridge the gap between raw economic data and actionable strategies, providing a platform that empowers
                professionals to navigate complex financial landscapes with clarity and confidence.
            </p>
            <p class="about-description">
                At the heart of Alterra is our commitment to innovation and precision. We integrate real-time data, advanced analytics,
                and cutting-edge technology to distill the essence of global economic trends. Whether it's understanding the implications
                of commodity price shifts, analyzing yield curve dynamics, or forecasting macroeconomic cycles, Alterra delivers insights
                tailored to your needs.
            </p>
            <p class="about-description">
                Much like the extraction of oil from the earth, Alterra digs deep into economic data to extract the most valuable insights.
                We don't just skim the surface—we get to the core of the economic trends that matter most to businesses and investors.
                With the right data, anything is possible. And just like oil, the true value is unlocked when we know where to dig.
            </p>
        </div>
        <div class="image-collage">
            <div class="image-1">
                <img src="{oil_digger_base64}" alt="Oil Digger" class="collage-image">
            </div>
            <div class="image-2">
                <img src="{wheat_field_base64}" alt="Wheat Field" class="collage-image">
            </div>
            <div class="image-3">
                <img src="{Mining_base64}" alt="Mining" class="collage-image">
            </div>
        </div>
    </div>

    <p class="closing-remarks">
        Alterra is dedicated to helping clients navigate complex financial landscapes, turn data into actionable insights,
        and ultimately drive success in an ever-changing world. We provide the tools and the knowledge necessary to make informed
        decisions that will lead to sustainable growth. Join us in unlocking the potential of economic intelligence.
    </p>
""", unsafe_allow_html=True)

# Close About Section
st.markdown('</div>', unsafe_allow_html=True)


# Footer (reused from economic page)
st.markdown(f"""
    <div style="background: #F8FAFC; padding: 2rem; margin-top: 3rem; text-align: center; border-top: 1px solid #E0E0E0;">
        <div style="color: #90A4AE; font-size: 0.9rem;">Powered by</div>
        <div style="color: #2E7D32; font-size: 1.2rem; font-weight: 600; margin-top: 0.5rem;">ALTERRA</div>
        <div style="color: #90A4AE; font-size: 0.8rem; margin-top: 1rem;">
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
    </div>
""", unsafe_allow_html=True)
