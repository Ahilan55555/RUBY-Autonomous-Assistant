from core.capability_registry_v2 import (
    has_capability
)


class PlannerValidator:

    def validate(
        self,
        plan
    ):
        if plan is None:

            return {
                "valid": False,
                "reason": "Planner returned no plan."
            }


        for task in plan.tasks:

            valid = has_capability(
                task.intent,
                task.target
            )

            if not valid:

                return {

                    "valid": False,

                    "reason": "Capability does not exist.",

                    "intent": task.intent,

                    "target": task.target

                }

        return {

            "valid": True

        }