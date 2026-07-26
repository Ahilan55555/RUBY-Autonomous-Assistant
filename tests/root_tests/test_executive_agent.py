from modules.agents.executive_agent import (
    ExecutiveAgent
)

from core.action_executor import (
    ActionExecutor
)

agent = ExecutiveAgent()

executor = ActionExecutor()

actions = agent.execute_goal(
    "open github"
)

print(actions)

print(
    executor.execute(
        actions
    )
)