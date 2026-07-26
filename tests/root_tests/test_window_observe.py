from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

print(
    agent.observe_window(
        "Firefox"
    )
)