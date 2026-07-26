from modules.capabilities.browser.search import BrowserSearchCapability
from modules.agents.goal_analyzer import GoalAnalyzer

capability = BrowserSearchCapability()

context = GoalAnalyzer().analyze(
    "search google robotics"
)

plan = capability.build_plan(
    context
)

print(plan.goal)
print(plan.tasks)