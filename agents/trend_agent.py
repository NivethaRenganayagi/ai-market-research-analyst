from tools.web_search import search_web
from tools.llm import generate_response

def trend_agent(company):

    results = search_web(
        f"{company} market trends industry trends growth"
    )

    combined_text = ""

    for r in results:
        combined_text += r["content"][:500] + "\n"

    prompt = f"""
    Analyze market and industry trends related to {company}.

    Mention:
    - growth trends
    - emerging opportunities
    - threats
    - future outlook

    DATA:
    {combined_text}

    Keep response concise.
    """

    return generate_response(prompt)