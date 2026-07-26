from modules.agents.desktop_assistant_agent import (
    DesktopAssistantAgent
)

agent = DesktopAssistantAgent()

agent.observe()

print(
    agent.project_status()
)