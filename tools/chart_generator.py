import matplotlib.pyplot as plt
import os
import random


def generate_competitor_chart(company, competitors):

    companies = [company] + competitors

    scores = []

    base = 85

    for i in range(len(companies)):

        scores.append(base - (i * 5))

    plt.figure(figsize=(8, 5))

    plt.bar(companies, scores)

    plt.title(f"{company} Competitor Comparison")
    plt.ylabel("Market Position Score")

    os.makedirs("outputs/charts", exist_ok=True)

    path = "outputs/charts/competitor_chart.png"

    plt.savefig(path)

    plt.close()

    return path


def generate_sentiment_chart(company):

    positive = random.randint(55, 80)
    neutral = random.randint(10, 25)

    negative = 100 - positive - neutral

    labels = ["Positive", "Neutral", "Negative"]

    sizes = [positive, neutral, negative]

    plt.figure(figsize=(6, 6))

    plt.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%"
    )

    plt.title(f"{company} Customer Sentiment")

    path = "outputs/charts/sentiment_chart.png"

    plt.savefig(path)

    plt.close()

    return path


def generate_pricing_chart(company, competitors):

    companies = [company] + competitors[:3]

    pricing = [
        random.randint(8, 20)
        for _ in companies
    ]

    plt.figure(figsize=(8, 5))

    plt.barh(companies, pricing)

    plt.title("Pricing Comparison")
    plt.xlabel("Monthly Price ($)")

    path = "outputs/charts/pricing_chart.png"

    plt.savefig(path)

    plt.close()

    return path