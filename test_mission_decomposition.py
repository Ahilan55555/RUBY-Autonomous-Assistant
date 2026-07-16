from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.mission_builder import MissionBuilder

context = GoalAnalyzer().analyze(
    "search robotics papers read summarize save"
)

mission = MissionBuilder().build(
    context
)

print(mission.goal)

print()

for step in mission.steps:

    print(step)
    