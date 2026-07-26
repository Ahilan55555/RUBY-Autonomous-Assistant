from modules.agents.desktop_assistant_agent import (
    DesktopAssistantAgent
)

agent = DesktopAssistantAgent()

result = agent.observe()

print(result)

print("\nTASK:")
print(agent.current_task())

print("\nRECENT:")
print(agent.recent_tasks())