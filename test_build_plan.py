from modules.agents.planner import Planner
from modules.agents.goal_analyzer import GoalAnalyzer

planner = Planner()

context = GoalAnalyzer().analyze(
    "search google robotics"
)

plan = planner.build_plan(
    "search",
    context
)

print(plan.goal)
print(plan.tasks)