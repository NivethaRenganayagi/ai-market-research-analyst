from tools.web_search import search_web
from tools.llm import generate_response


def competitor_agent(company):

    results = search_web(
        f"{company} competitors market rivals"
    )

    combined_text = ""

    for r in results:
        combined_text += r["content"][:400] + "\n"

    prompt = f"""
    Identify the top 3 competitors of {company}.

    Return ONLY in this format:

    Competitors:
    1. competitor name
    2. competitor name
    3. competitor name

    Also provide a short competitor summary.

    DATA:
    {combined_text}
    """

    response = generate_response(prompt)

    competitors = []

    for line in response.split("\n"):

        if "." in line:

            parts = line.split(".", 1)

            if len(parts) > 1:

                competitors.append(
                    parts[1].strip()
                )

    competitors = competitors[:3]

    return {
        "summary": response,
        "competitors": competitors
    }