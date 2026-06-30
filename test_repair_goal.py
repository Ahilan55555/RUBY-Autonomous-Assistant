from modules.agents.autonomous_agent import (
    AutonomousAgent
)

agent = AutonomousAgent()

print(
    agent.create_repair_goal(
        "click Ask",
        "Ask"
    )
)