import core.register_capabilities

from modules.agents.desktop_agent import (
    DesktopAgent
)

agent = DesktopAgent()

result = agent.run_and_verify(
    "focus firefox",
    "ChatGPT"
)

print(result)