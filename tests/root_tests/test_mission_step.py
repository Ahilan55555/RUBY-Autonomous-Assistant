from core.mission_step import MissionStep

step = MissionStep(
    action="search",
    target="robotics papers"
)

print(step)

step.completed()

print(step)