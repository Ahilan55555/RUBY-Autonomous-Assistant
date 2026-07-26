import core.register_capabilities

from modules.agents.workflow_agent import (
    WorkflowAgent
)

agent = WorkflowAgent()

agent.run_workflow(
    "focus_firefox"
)

print(
    agent.verify_text(
        "ChatGPT"
    )
)