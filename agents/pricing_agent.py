from tools.web_search import search_web
from tools.llm import generate_response

def pricing_agent(company):

    results = search_web(
        f"{company} pricing plans competitors pricing"
    )

    combined_text = ""

    for r in results:
        combined_text += r["content"][:500] + "\n"

    prompt = f"""
    Analyze the pricing strategy of {company}.

    Compare pricing with competitors.

    Mention:
    - pricing tiers
    - affordability
    - premium vs budget positioning

    DATA:
    {combined_text}

    Keep response concise.
    """

    return generate_response(prompt)