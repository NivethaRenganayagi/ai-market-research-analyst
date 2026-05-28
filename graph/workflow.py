import asyncio

from agents.competitor_agent import competitor_agent
from agents.pricing_agent import pricing_agent
from agents.sentiment_agent import sentiment_agent
from agents.trend_agent import trend_agent

from agents.analyst_agent import analyst_agent
from agents.writer_agent import writer_agent


async def run_analysis(company):

    loop = asyncio.get_event_loop()

    competitor_task = loop.run_in_executor(
        None,
        competitor_agent,
        company
    )

    pricing_task = loop.run_in_executor(
        None,
        pricing_agent,
        company
    )

    sentiment_task = loop.run_in_executor(
        None,
        sentiment_agent,
        company
    )

    trend_task = loop.run_in_executor(
        None,
        trend_agent,
        company
    )

    competitor_result, pricing_result, sentiment_result, trend_result = await asyncio.gather(
        competitor_task,
        pricing_task,
        sentiment_task,
        trend_task
    )

    research_data = {
        "competitor_analysis": competitor_result["summary"],
        "pricing_analysis": pricing_result,
        "sentiment_analysis": sentiment_result,
        "trend_analysis": trend_result
    }

    analysis = analyst_agent(
        research_data,
        company
    )

    final_report = writer_agent(
        company,
        analysis
    )

    return {
        "research_data": research_data,
        "analysis": analysis,
        "final_report": final_report,
        "competitors": competitor_result["competitors"]
    }