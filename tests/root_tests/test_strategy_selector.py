from modules.agents.goal_analyzer import GoalAnalyzer
from modules.agents.strategy_selector import StrategySelector

analyzer = GoalAnalyzer()

selector = StrategySelector()

context = analyzer.analyze(
    "search google robotics"
)

strategy = selector.choose(
    context
)

print(strategy)