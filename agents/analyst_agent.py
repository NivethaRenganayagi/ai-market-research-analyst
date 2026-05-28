from tools.llm import generate_response

def analyst_agent(data, company):

    prompt = f"""
    You are a senior market research analyst.

    Analyze the research findings for {company}.

    Provide concise strategic insights covering:

    1. Main competitors
    2. Pricing positioning
    3. Customer sentiment summary
    4. Key market trends
    5. Major opportunities
    6. Key risks

    Keep the response concise and insight-focused.
    Avoid detailed formatting or long explanations.

    DATA:

    Competitor Analysis:
    {data['competitor_analysis']}

    Pricing Analysis:
    {data['pricing_analysis']}

    Sentiment Analysis:
    {data['sentiment_analysis']}

    Trend Analysis:
    {data['trend_analysis']}
    """

    return generate_response(prompt)