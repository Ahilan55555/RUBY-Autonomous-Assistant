from core.mission_context import MissionContext


class Mission:

    def __init__(
        self,
        goal=""
    ):

        self.goal = goal

        self.steps = []

        self.plans = []

        self.context = MissionContext()

        self.status = "pending"

    def add_step(
        self,
        step
    ):

        self.steps.append(
            step
        )

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

            f"steps={len(self.steps)}, "

            f"plans={len(self.plans)}, "

            f"status={self.status}"

            f")"

        )