class StrategySelector:

    def choose(
        self,
        goal_context
    ):

        if goal_context.domain == "coding":

            return "coding"

        if goal_context.difficulty == "easy":

            return "fast"

        if goal_context.difficulty == "medium":

            return "deep"

        return "fast"