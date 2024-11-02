from swarm import Agent

def analyze_sentiment(context_variables):
    report_text = context_variables["report_text"]
    sentiment = "positive" if "profit" in report_text else "negative"
    return f"The sentiment of the report is: {sentiment}"

sentiment_agent = Agent(
    name="Sentiment Agent",
    instructions="Analyze the sentiment of the report.",
    functions=[analyze_sentiment]
)
