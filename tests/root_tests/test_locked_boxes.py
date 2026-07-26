# test_locked_boxes.py

from modules.agents.desktop_agent import (
    DesktopAgent
)
import core.register_capabilities
agent = DesktopAgent()

agent.run(
    "focus firefox"
)

boxes = (
    agent.observe_locked_window_boxes()
)

print(boxes[:50])