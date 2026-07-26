from modules.agents.executive_agent import (
    ExecutiveAgent
)

from core.action_executor import (
    ActionExecutor
)

goal = (
    "create python project calculator"
)

agent = ExecutiveAgent()

executor = ActionExecutor()

actions = (
    agent.execute_goal(
        goal
    )
)

print(actions)

print(
    executor.execute(
        actions
    )
)