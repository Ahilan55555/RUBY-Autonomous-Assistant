import core.register_capabilities

from modules.agents.autonomous_agent import (
    AutonomousAgent
)

agent = AutonomousAgent()

print(
    agent.run_goal(
        "ask chatgpt what is robotics",
        "robotics"
    )
)