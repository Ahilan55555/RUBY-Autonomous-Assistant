# test_repair_execution.py

from modules.agents.autonomous_agent import (
    AutonomousAgent
)

agent = AutonomousAgent()

print(
    agent.run_goal(
        "click ZZZZZZZZZ",
        "Ask"
    )
)