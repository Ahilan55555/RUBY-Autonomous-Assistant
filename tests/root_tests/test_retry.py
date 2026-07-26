import core.register_capabilities

from modules.agents.workflow_agent import (
    WorkflowAgent
)

agent = WorkflowAgent()

task = {
    "intent": "window",
    "target": "focus",
    "query": "Firefox"
}

print(
    agent.retry_until_visible(
        task,
        "ChatGPT"
    )
)