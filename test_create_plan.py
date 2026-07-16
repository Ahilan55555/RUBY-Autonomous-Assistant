from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.mission_builder import MissionBuilder
from modules.agents.planner import Planner


analyzer = GoalAnalyzer()

context = analyzer.analyze(
    "search google robotics"
)

builder = MissionBuilder()

mission = builder.build(
    context
)

planner = Planner()

goal = planner.create_plan(
    mission.steps[0],
    context
)

print(goal)