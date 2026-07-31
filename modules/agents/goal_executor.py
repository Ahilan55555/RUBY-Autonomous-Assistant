from core.executor import Executor

from core.world_state import (
    update_state
)


class GoalExecutor:

    def __init__(self):

        self.executor = Executor()

    def run(
        self,
        plan
    ):

        update_state(
            "last_goal",
            plan.goal
        )

        for task in plan.tasks:

            update_state(
                "last_task",
                task.name
            )

            result = self.executor.execute_queue(
                task.action_queue
            )

            if not result["success"]:

                update_state(
                    "last_result",
                    "failed"
                )

                return result

        update_state(
            "last_result",
            "success"
        )

        return {

            "success": True

        }