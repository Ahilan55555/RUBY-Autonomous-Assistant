from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.mission_builder import MissionBuilder

context = GoalAnalyzer().analyze(
    "search robotics papers read summarize save"
)

mission = MissionBuilder().build(
    context
)

mission.context.set(
    "query",
    "robotics papers"
)

print(mission)

print(mission.context.get("query"))

print(mission.steps)