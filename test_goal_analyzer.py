from modules.agents.goal_analyzer import GoalAnalyzer

analyzer = GoalAnalyzer()

context = analyzer.analyze(
    "search google robotics"
)

print(context)