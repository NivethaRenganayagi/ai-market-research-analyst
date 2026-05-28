import streamlit as st
import asyncio
from datetime import datetime

from graph.workflow import run_analysis

from tools.chart_generator import (
    generate_competitor_chart,
    generate_sentiment_chart,
    generate_pricing_chart
)

from tools.pdf_generator import generate_pdf


# ====================================
# PAGE CONFIG
# ====================================

st.set_page_config(
    page_title="AI Market Research Analyst",
    page_icon="📊",
    layout="wide"
)


# ====================================
# CUSTOM CSS
# ====================================

st.markdown("""
<style>

.main {
    background-color: #0E1117;
    color: white;
}

.stTextInput > div > div > input {
    background-color: #1E1E1E;
    color: white;
    border-radius: 10px;
    border: 1px solid #333;
}

.stButton > button {
    background: linear-gradient(to right, #7F5AF0, #2CB67D);
    color: white;
    border-radius: 12px;
    border: none;
    padding: 0.6rem 1.5rem;
    font-weight: bold;
}

.stButton > button:hover {
    opacity: 0.9;
}

.block-container {
    padding-top: 2rem;
}

.metric-card {
    background-color: #161B22;
    padding: 1rem;
    border-radius: 15px;
    text-align: center;
    border: 1px solid #2A2F3A;
}

.footer {
    text-align: center;
    color: gray;
    margin-top: 50px;
}

</style>
""", unsafe_allow_html=True)


# ====================================
# SIDEBAR
# ====================================

st.sidebar.title("🤖 AI Market Research Analyst")

st.sidebar.markdown("""
### Features
- Multi-Agent AI Workflow
- Parallel Research Agents
- SWOT Analysis
- Dynamic Visual Analytics
- PDF Report Generation
- Market Trend Insights
""")

st.sidebar.markdown("---")

st.sidebar.info(
    "Built using LangGraph + CrewAI + Groq + Streamlit"
)


# ====================================
# HEADER
# ====================================

st.markdown("""
# 📊 AI Market Research Analyst

Generate autonomous competitive intelligence reports
with AI-powered market analysis, SWOT insights,
and dynamic visual analytics.
""")


# ====================================
# INPUT SECTION
# ====================================

company = st.text_input(
    "Enter a company or product name",
    placeholder="Example: Spotify, Notion, Tesla..."
)


# ====================================
# GENERATE BUTTON
# ====================================

if st.button("🚀 Generate Market Report"):

    if not company.strip():

        st.warning("Please enter a company or product name.")

    else:

        try:

            with st.spinner("AI agents are researching the market..."):

                result = asyncio.run(
                    run_analysis(company)
                )

                competitors = result.get(
                    "competitors",
                    []
                )

                if len(competitors) == 0:

                    competitors = [
                        "Competitor 1",
                        "Competitor 2",
                        "Competitor 3"
                    ]

                competitor_chart = generate_competitor_chart(
                    company,
                    competitors
                )

                sentiment_chart = generate_sentiment_chart(
                    company
                )

                pricing_chart = generate_pricing_chart(
                    company,
                    competitors
                )

                pdf_path = generate_pdf(
                    company,
                    result["final_report"]
                )

            st.success(
                "✅ Market Research Report Generated"
            )

            # ====================================
            # METRICS SECTION
            # ====================================

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class="metric-card">
                    <h3>Competitors</h3>
                    <h2>{len(competitors)}</h2>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown("""
                <div class="metric-card">
                    <h3>Report Status</h3>
                    <h2>Ready</h2>
                </div>
                """, unsafe_allow_html=True)

            with col3:

                current_time = datetime.now().strftime("%H:%M:%S")

                st.markdown(f"""
                <div class="metric-card">
                    <h3>Generated At</h3>
                    <h2>{current_time}</h2>
                </div>
                """, unsafe_allow_html=True)

            st.markdown("---")

            # ====================================
            # FINAL REPORT
            # ====================================

            st.subheader("📄 Final Market Research Report")

            st.write(result["final_report"])

            st.markdown("---")

            # ====================================
            # VISUAL ANALYTICS
            # ====================================

            st.subheader("📈 Visual Analytics")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.image(
                    competitor_chart,
                    caption="Competitor Comparison"
                )

            with col2:
                st.image(
                    sentiment_chart,
                    caption="Customer Sentiment"
                )

            with col3:
                st.image(
                    pricing_chart,
                    caption="Pricing Comparison"
                )

            st.markdown("---")

            # ====================================
            # DOWNLOAD BUTTON
            # ====================================

            with open(pdf_path, "rb") as f:

                st.download_button(
                    "⬇ Download PDF Report",
                    f,
                    file_name=f"{company}_market_report.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                "⚠ An error occurred while generating the report."
            )

            st.exception(e)


# ====================================
# FOOTER
# ====================================

st.markdown("""
<div class="footer">
Built with LangGraph + CrewAI + Groq + Streamlit
</div>
""", unsafe_allow_html=True)