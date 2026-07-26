import core.register_capabilities

from modules.agents.autonomous_agent import (
    AutonomousAgent
)

agent = AutonomousAgent()

agent.run(
    "focus firefox"
)