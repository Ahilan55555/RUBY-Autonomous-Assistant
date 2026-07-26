from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.mission_builder import MissionBuilder
from modules.agents.mission_executor import MissionExecutor

context = GoalAnalyzer().analyze(
    "search robotics papers"
)

mission = MissionBuilder().build(
    context
)

executor = MissionExecutor()

result = executor.run(
    mission
)

print(result)

print(mission.status)

for step in mission.steps:
    print(step)