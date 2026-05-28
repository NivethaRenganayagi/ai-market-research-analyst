from tools.web_search import search_web
from tools.llm import generate_response

def sentiment_agent(company):

    results = search_web(
        f"{company} customer reviews user feedback sentiment"
    )

    combined_text = ""

    for r in results:
        combined_text += r["content"][:500] + "\n"

    prompt = f"""
    Analyze customer sentiment for {company}.

    Identify:
    - common positives
    - common complaints
    - overall satisfaction

    DATA:
    {combined_text}

    Keep it concise.
    """

    return generate_response(prompt)