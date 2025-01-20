import streamlit as st
from datetime import datetime
import os
import base64

# Configure Streamlit page
st.set_page_config(
    page_title="Alterra | Home",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Get the absolute path to the image file
image_path = os.path.join(os.getcwd(), 'plots', 'sp500_gdp.png')

# Function to encode image to base64
def image_to_base64(image_path):
    with open(image_path, "rb") as img_file:
        encoded_image = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{encoded_image}"

# Get the base64 encoded image
image_base64 = image_to_base64(image_path)

# Reuse the same CSS styles from the economic page with additional homepage-specific styles
st.markdown(f"""
    <style>
        /* Sidebar Styles */
        [data-testid="stSidebar"] {{
            background-color: #FAFAFA;
            border-right: 1px solid #E0E0E0;
            padding-top: 1rem;
        }}
        
        .main {{
            background-color: #FFFFFF;
        }}
        
        /* Hero Section Styles */
        .hero-container {{
            position: relative;
            padding: 6rem 2rem;
            text-align: center;
            margin: -4rem -4rem 1rem -4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            color: white;
            background-image: url("{image_base64}");
            background-size: 100% 80%; /* Adjust the size of the image vertically */
            background-position: center 0%; /* Move the image down */
            background-repeat: no-repeat;
        }}

        /* Hero Title Styles */
        .company-title {{
            font-size: 6rem;
            font-weight: 700;
            color: #2E7D32; /* Dark green title */
            letter-spacing: -1px;
            margin-bottom: 1rem;
            z-index: 2; /* Ensure the title is above the image */
            margin-top: -40rem;
        }}
        
        .company-subtitle {{
            font-size: 2rem;
            color: #2E7D32;
            max-width: 800px;
            margin: 0 auto;
            z-index: 2;
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
            padding: 1.5rem;
            border: 1px solid #E0E0E0;
            transition: all 0.3s ease;
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
            cursor: pointer;
        }}
        
        .insight-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15);
        }}
        
        .insight-title {{
            font-size: 1.2rem;
            color: #2E7D32;
            font-weight: 600;
        }}
        
        .insight-content {{
            font-size: 1.0rem;
            color: #262626;
            margin-top: 0.5rem;
        }}
        
        .insight-footer {{
            font-size: 0.9rem;
            color: #90A4AE;
            display: flex;
            justify-content: space-between;
            margin-top: 1rem;
        }}
        
        .insight-impact {{
            color: #2E7D32;
            font-weight: 600;
        }}

        /* Market Insights header */
        .market-insights-header {{
            margin-bottom: 0.5rem;
            margin-top: -25rem;
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
    st.markdown("### Market Insights", unsafe_allow_html=True)
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
    <h2 class="market-insights-header" style="color: #2E7D32; font-size: 2rem; margin-bottom: 0.5rem; margin-top: -20rem;">
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
                <div class="insight-impact">Medium</div>
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

# About Section
st.markdown("""
    <div class="about-section">
        <h2 style="color: #2E7D32; font-size: 2rem; text-align: center; margin-bottom: 2rem;">
            Empowering Economic Decision Making
        </h2>
        <p style="color: #262626; text-align: center; max-width: 800px; margin: 0 auto; font-size: 1.1rem; line-height: 1.6;">
            Alterra delivers cutting-edge economic intelligence through advanced analytics, 
            real-time market insights, and comprehensive data analysis. Our platform enables 
            leaders to make informed decisions in an ever-evolving global economy.
        </p>
        <div class="feature-grid">
            <div class="feature-card">
                <div style="font-size: 2rem; color: #2E7D32; margin-bottom: 1rem;">🎯</div>
                <h3 style="color: #2E7D32; margin-bottom: 0.5rem;">Precision Analytics</h3>
                <p style="color: #666666;">Advanced algorithms delivering accurate market predictions</p>
            </div>
            <div class="feature-card">
                <div style="font-size: 2rem; color: #2E7D32; margin-bottom: 1rem;">⚡</div>
                <h3 style="color: #2E7D32; margin-bottom: 0.5rem;">Real-Time Data</h3>
                <p style="color: #666666;">Instant access to global market movements</p>
            </div>
            <div class="feature-card">
                <div style="font-size: 2rem; color: #2E7D32; margin-bottom: 1rem;">📈</div>
                <h3 style="color: #2E7D32; margin-bottom: 0.5rem;">Strategic Insights</h3>
                <p style="color: #666666;">Actionable intelligence for informed decision-making</p>
            </div>
            <div class="feature-card">
                <div style="font-size: 2rem; color: #2E7D32; margin-bottom: 1rem;">🔒</div>
                <h3 style="color: #2E7D32; margin-bottom: 0.5rem;">Enterprise Security</h3>
                <p style="color: #666666;">Bank-grade protection for your sensitive data</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)

# Footer (reused from economic page)
st.markdown(f"""
    <div style="background: #F8FAFC; padding: 2rem; margin-top: 3rem; text-align: center; border-top: 1px solid #E0E0E0;">
        <div style="color: #90A4AE; font-size: 0.9rem;">Powered by</div>
        <div style="color: #2E7D32; font-size: 1.2rem; font-weight: 600; margin-top: 0.5rem;">ALTERRA</div>
        <div style="color: #90A4AE; font-size: 0.8rem; margin-top: 1rem;">
            Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}</div>
    </div>
""", unsafe_allow_html=True)
