from swarm import Swarm
from agents.summary_agent import summary_agent
from agents.sentiment_agent import sentiment_agent
from agents.recommendation_agent import recommendation_agent
from utils.helpers import load_earnings_report
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Set the OpenAI API key from the environment variable
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

# Initialize Swarm client
client = Swarm()

# Load earnings report
report_text = load_earnings_report("sample_earnings.txt")

# Run summary agent
response = client.run(
    agent=summary_agent,
    messages=[{"role": "user", "content": "Summarize the report"}],
    context_variables={"report_text": report_text}
)
print(response.messages[-1]["content"])

# Pass summary to sentiment agent
response = client.run(
    agent=sentiment_agent,
    messages=[{"role": "user", "content": "Analyze the sentiment"}],
    context_variables={"report_text": report_text}
)
print(response.messages[-1]["content"])

# Extract sentiment and run recommendation agent
sentiment = response.messages[-1]["content"].split(": ")[-1].strip()
response = client.run(
    agent=recommendation_agent,
    messages=[{"role": "user", "content": "Give a recommendation"}],
    context_variables={"sentiment": sentiment}
)
print(response.messages[-1]["content"])
