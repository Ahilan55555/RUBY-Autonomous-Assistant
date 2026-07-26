from modules.agents.llm_planner import (
    LLMPlanner
)

planner = LLMPlanner()

plan = planner.plan(
    "open github"
)

print(plan.tasks)