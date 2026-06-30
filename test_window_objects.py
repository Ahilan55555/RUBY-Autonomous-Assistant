# test_window_objects.py

import core.register_capabilities

from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

agent.lock_active_window()

print(
    agent.observe_locked_window_objects()
)