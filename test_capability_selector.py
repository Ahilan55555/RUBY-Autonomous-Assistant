from modules.agents.capability_selector import CapabilitySelector
from modules.agents.goal_analyzer import GoalAnalyzer

selector = CapabilitySelector()

context = GoalAnalyzer().analyze(
    "search google robotics"
)

print(
    selector.choose(
        "search",
        context
    )
)