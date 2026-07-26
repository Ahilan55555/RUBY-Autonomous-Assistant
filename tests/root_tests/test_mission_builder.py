from core.goal_context import GoalContext
from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.mission_builder import MissionBuilder


analyzer = GoalAnalyzer()

context = analyzer.analyze(
    "search google robotics"
)

builder = MissionBuilder()

mission = builder.build(
    context
)

print(mission.goal)

print(mission.steps)