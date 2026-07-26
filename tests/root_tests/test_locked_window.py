from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

agent.lock_active_window()

print(
    "WINDOW ID:",
    agent.target_window_id
)

result = agent.observe_locked_window()

print(result)

print(
    len(result)
)