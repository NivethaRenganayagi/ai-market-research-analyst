from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Image,
    PageBreak
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

import os


def generate_pdf(company, report_text):

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    safe_name = (
        company
        .replace(" ", "_")
        .lower()
    )

    pdf_path = (
        f"outputs/reports/"
        f"{safe_name}_market_report.pdf"
    )

    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    elements = []

    # =========================
    # TITLE
    # =========================

    title = Paragraph(
        f"<b>{company} Market Research Report</b>",
        styles['Title']
    )

    elements.append(title)

    elements.append(
        Spacer(1, 20)
    )

    # =========================
    # REPORT CONTENT
    # =========================

    formatted_report = (
        report_text
        .replace("\n", "<br/>")
    )

    report_paragraph = Paragraph(
        formatted_report,
        styles['BodyText']
    )

    elements.append(
        report_paragraph
    )

    elements.append(
        Spacer(1, 20)
    )

    # =========================
    # CHARTS SECTION
    # =========================

    charts_title = Paragraph(
        "<b>Visual Analytics</b>",
        styles['Heading2']
    )

    elements.append(
        charts_title
    )

    elements.append(
        Spacer(1, 15)
    )

    charts = [
        (
            "Competitor Comparison",
            "outputs/charts/competitor_chart.png"
        ),

        (
            "Customer Sentiment",
            "outputs/charts/sentiment_chart.png"
        ),

        (
            "Pricing Comparison",
            "outputs/charts/pricing_chart.png"
        )
    ]

    for chart_title, chart_path in charts:

        if os.path.exists(chart_path):

            chart_heading = Paragraph(
                f"<b>{chart_title}</b>",
                styles['Heading3']
            )

            elements.append(
                chart_heading
            )

            elements.append(
                Spacer(1, 10)
            )

            img = Image(
                chart_path,
                width=300,
                height=180
            )

            elements.append(img)

            elements.append(
                Spacer(1, 20)
            )

    # =========================
    # BUILD PDF
    # =========================

    doc.build(elements)

    return pdf_path