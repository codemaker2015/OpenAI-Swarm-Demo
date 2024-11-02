from swarm import Agent

def generate_recommendation(context_variables):
    sentiment = context_variables["sentiment"]
    recommendation = "Buy" if sentiment == "positive" else "Hold"
    return f"My recommendation is: {recommendation}"

recommendation_agent = Agent(
    name="Recommendation Agent",
    instructions="Recommend actions based on the sentiment analysis.",
    functions=[generate_recommendation]
)
