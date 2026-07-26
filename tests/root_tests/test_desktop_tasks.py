from modules.agents.desktop_assistant_agent import (
    DesktopAssistantAgent
)

agent = DesktopAssistantAgent()

result = agent.observe()

print()

print(
    "CURRENT TASK:"
)

print(
    agent.current_task()
)

print()

print(
    "RECENT TASKS:"
)

print(
    agent.recent_tasks()
)