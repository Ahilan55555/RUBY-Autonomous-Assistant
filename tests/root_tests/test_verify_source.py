# test_verify_source.py

from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

print(
    agent.observe_locked_window()
)