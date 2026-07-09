from core.task import Task


class Plan:

    def __init__(
        self,
        goal=""
    ):

        self.goal = goal
        self.tasks = []
        self.status = "created"

    def add_task(
        self,
        task
    ):

        self.tasks.append(task)

    def started(
        self
    ):

        self.status = "running"

    def finished(
        self
    ):

        self.status = "completed"