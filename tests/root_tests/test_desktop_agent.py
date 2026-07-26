import core.register_capabilities

from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

agent.run(
    "focus firefox"
)

agent.run(
    "click Ask"
)

agent.run(
    "type hello in Ask"
)