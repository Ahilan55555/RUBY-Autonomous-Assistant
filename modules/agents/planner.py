from core.goal import Goal


class Planner:

    def interpret(
        self,
        text
    ):

        text = text.lower()

        if text.startswith("search google"):

            query = (

                text.replace(

                    "search google",

                    ""

                )

                .strip()

            )

            return Goal(

                action="search",

                target="google",

                data=query

            )

        return None