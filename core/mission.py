class Mission:

    def __init__(
        self,
        goal=""
    ):

        self.goal = goal

        self.plans = []

        self.status = "pending"


    def add_plan(
        self,
        plan
    ):

        self.plans.append(
            plan
        )


    def started(
        self
    ):

        self.status = "running"


    def finished(
        self
    ):

        self.status = "completed"


    def __repr__(
        self
    ):

        return (

            f"Mission("

            f"goal={self.goal}, "

            f"plans={len(self.plans)}"

            f")"

        )