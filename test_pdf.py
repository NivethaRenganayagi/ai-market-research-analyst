import asyncio

from graph.workflow import run_analysis
from tools.chart_generator import *
from tools.pdf_generator import generate_pdf


result = asyncio.run(
    run_analysis("Notion")
)

generate_competitor_chart()
generate_sentiment_chart()
generate_pricing_chart()

pdf_path = generate_pdf(
    result["final_report"]
)

print(f"PDF generated: {pdf_path}")