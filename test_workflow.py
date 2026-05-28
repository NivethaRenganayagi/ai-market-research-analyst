import asyncio
from graph.workflow import run_analysis

result = asyncio.run(
    run_analysis("Notion")
)

print("\nFINAL REPORT:\n")
print(result["final_report"])