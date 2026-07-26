from modules.agents.planner import Planner
from modules.agents.goal_executor import GoalExecutor


class MissionExecutor:

    def __init__(self):

        self.planner = Planner()

        self.goal_executor = GoalExecutor()

    def run(
        self,
        mission
    ):

        mission.started()

        for step in mission.steps:

            capability, plan = self.planner.build_plan(
                step,
                mission
            )

            if capability is None or plan is None:

                step.failed()

                return {
                    "success": False,
                    "error": f"Could not build plan for {step.action}"
                }

            capability.prepare(
                step,
                mission
            )

            result = self.goal_executor.run(
                plan
            )

            capability.collect_result(
                mission,
                result.get("observation")
            )

            capability.cleanup(
                mission
            )

            if not result["success"]:

                step.failed()

                return result

            step.completed(
                result.get("data")
            )

        mission.finished()

        return {
            "success": True
        }