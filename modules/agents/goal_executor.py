from core.executor import Executor

from core.world_state import (
    update_state
)

from modules.agents.task_observer import (
    TaskObserver
)

from modules.agents.decision_engine import (
    DecisionEngine
)

from core.observation import Observation

class GoalExecutor:

    def __init__(
        self
    ):

        self.executor = Executor()

        self.observer = TaskObserver()

        self.decision_engine = DecisionEngine()


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

            observation = self.observer.observe(
                task
            )

            decision = self.decision_engine.decide(

                task,

                observation

            )

            if decision["action"] != "continue":

                update_state(

                    "last_result",

                    decision["action"]

                )

                return {

                    "success": False,

                    "decision": decision,

                    "observation": observation

                }

        update_state(
            "last_result",
            "success"
        )

        observation = Observation()

        return {

            "success": True,

            "observation": observation

        }