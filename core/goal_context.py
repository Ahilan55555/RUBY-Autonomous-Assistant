class GoalContext:

    def __init__(
        self,
        command
    ):

        self.command = command

        self.domain = None

        self.intent = None

        self.difficulty = None

        self.strategy = None

        self.needs = []

    def __repr__(
        self
    ):

        return (

            f"GoalContext("

            f"command={self.command}, "

            f"domain={self.domain}, "

            f"intent={self.intent}, "

            f"difficulty={self.difficulty}, "

            f"strategy={self.strategy}, "

            f"needs={self.needs}"

            f")"

        )