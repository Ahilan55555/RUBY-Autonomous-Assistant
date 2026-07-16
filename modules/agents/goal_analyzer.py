from core.goal_context import GoalContext

from modules.agents.strategy_selector import StrategySelector



class GoalAnalyzer:

    def analyze(
        self,
        command
    ):

        context = GoalContext(
            command
        )

        text = command.lower()

        # ---------- Domain ----------

        if any(

            word in text

            for word in [

                "google",

                "youtube",

                "browser",

                "firefox",

                "chatgpt"

            ]

        ):

            context.domain = "browser"

        elif any(

            word in text

            for word in [

                "python",

                "code",

                "program",

                "function",

                "class",

                "bug"

            ]

        ):

            context.domain = "coding"

        else:

            context.domain = "general"

        # ---------- Intent ----------

        if "search" in text:

            context.intent = "search"

        elif "play" in text:

            context.intent = "play"

        elif "open" in text:

            context.intent = "open"

        elif "summarize" in text:

            context.intent = "summarize"

        else:

            context.intent = "unknown"

        # ---------- Difficulty ----------

        if len(

            text.split()

        ) <= 5:

            context.difficulty = "easy"

        else:

            context.difficulty = "medium"

        # ---------- Needs ----------

        context.needs = []

        if context.domain == "browser":

            context.needs.append(
                "browser"
            )

            context.needs.append(
                "internet"
            )

        selector = StrategySelector()

        context.strategy = selector.choose(
            context
        )

        return context