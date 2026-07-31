"""
Pipeline Executor

Runs the complete lifecycle of a capability.

Lifecycle

prepare()
↓

build_plan()
↓

execute_plan()
↓

observe()
↓

interpret()
↓

decide()
↓

apply_result()
↓

cleanup()
"""

from core.executor import Executor


class PipelineExecutor:

    def __init__(self):
        self.executor = Executor()

    def run(
        self,
        capability,
        step,
        mission=None
    ):

        capability.prepare(
            step,
            mission
        )

        plan = capability.build_plan(
            step,
            mission
        )

        if plan is None:
            return {
                "success": False,
                "error": "Unable to build plan"
            }

        for task in plan.tasks:

            execution = self.executor.execute_queue(
                task.action_queue
            )

            if isinstance(execution, dict):
                if not execution.get("success", False):
                    capability.cleanup(mission)
                    return execution

            elif execution is False:
                capability.cleanup(mission)
                return {
                    "success": False,
                    "error": f"Task '{task.name}' failed."
                }

        observation = capability.observe()

        interpretation = capability.interpret(
            observation
        )

        decision = capability.decide(
            interpretation,
            mission
        )

        result = capability.apply_result(
            mission,
            decision
        )

        capability.cleanup(
            mission
        )

        return result