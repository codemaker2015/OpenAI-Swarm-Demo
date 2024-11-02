from swarm import Agent

def summarize_report(context_variables):
    report_text = context_variables["report_text"]
    return f"Summary: {report_text[:1000]}..."

summary_agent = Agent(
    name="Summary Agent",
    instructions="Summarize the key points of the earnings report.",
    functions=[summarize_report]
)
