import core.register_capabilities

from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

agent.run(
    "focus firefox"
)