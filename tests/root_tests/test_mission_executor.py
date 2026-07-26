from core.mission import Mission
from core.plan import Plan


mission = Mission(
    goal="Research Robotics"
)

mission.add_plan(
    Plan(
        goal="Search Google"
    )
)

mission.add_plan(
    Plan(
        goal="Summarize"
    )
)

print(mission)

print(mission.plans)