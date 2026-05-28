from tools.llm import generate_response


def writer_agent(company, analysis):

    prompt = f"""
    You are a professional business report writer.

    Create a concise market research report for {company}.
    Limit each section to 3-4 concise bullet points.

    Include these sections:

    1. Executive Summary
    2. Competitor Landscape
    3. Pricing Analysis
    4. Customer Sentiment
    5. Market Trends
    6. SWOT Analysis
    7. Strategic Recommendations

    For SWOT, include:
    - 3 strengths
    - 3 weaknesses
    - 3 opportunities
    - 3 threats

    Keep the report:
    - concise
    - readable
    - insight-focused

    Avoid unnecessary long explanations.

    ANALYSIS:
    {analysis}
    """

    return generate_response(prompt)