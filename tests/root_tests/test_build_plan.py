from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.mission_builder import MissionBuilder
from modules.agents.planner import Planner

context = GoalAnalyzer().analyze(
    "search robotics papers"
)

mission = MissionBuilder().build(
    context
)

planner = Planner()

step = mission.steps[0]

capability, plan = planner.build_plan(
    step,
    mission
)
print(step)
print(type(capability).__name__)
print(plan.goal)
print(plan.tasks)
