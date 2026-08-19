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

        # ---------------------------------
        # EXECUTE PLAN
        # ---------------------------------

        for task in plan.tasks:

            if task.capability is not None:

                execution = capability.execute(
                    task,
                    mission
                )

            elif task.action_queue is not None:

                execution = self.executor.execute_queue(
                    task.action_queue
                )

            else:

                execution = {
                    "success": False,
                    "error": (
                        f"Task '{task.name}' has "
                        "no capability or action queue."
                    )
                }

            if isinstance(execution, dict):

                if not execution.get(
                    "success",
                    False
                ):

                    capability.cleanup(
                        mission
                    )

                    return execution

            elif execution is False:

                capability.cleanup(
                    mission
                )

                return {
                    "success": False,
                    "error": f"Task '{task.name}' failed."
                }


        # ---------------------------------
        # OBSERVE
        # ---------------------------------

        observation = capability.observe()

        interpretation = capability.interpret(
            observation
        )

        decision = capability.decide(
            interpretation,
            mission
        )


        # ---------------------------------
        # ACTION-ONLY CAPABILITY
        # ---------------------------------

        if decision is None:

            capability.cleanup(
                mission
            )

            return {
                "success": True,
                "result": {
                    "action": "completed",
                    "reason": "Capability executed successfully."
                }
            }


        # ---------------------------------
        # DECISION-BASED CAPABILITY
        # ---------------------------------

        result = capability.apply_result(
            mission,
            decision
        )

        decision_data = {

            "action": decision.action,

            "reason": decision.reason

        }

        capability.cleanup(
            mission
        )

        return {

            "success": (
                decision.action == "continue"
            ),

            "decision": decision_data,

            "result": result

        }