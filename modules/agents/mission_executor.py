from modules.agents.planner import Planner
from modules.agents.goal_executor import GoalExecutor
from modules.agents.decision_engine import DecisionEngine


class MissionExecutor:

    def __init__(self):

        self.planner = Planner()

        self.goal_executor = GoalExecutor()

        self.decision_engine = DecisionEngine()

    def run(
        self,
        mission
    ):
        print(">>> MissionExecutor.run() called")
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

            if not result["success"]:

                step.failed()

                return result

            observation = capability.observe()

            interpretation = capability.interpret(
                observation
            )

            decision = self.decision_engine.decide(
                step,
                interpretation
            )

            if decision.action != "continue":

                step.failed()

                return decision

            capability.apply_result(
                mission,
                interpretation
            )

            capability.cleanup(
                mission
            )

            step.completed(
                result.get("data")
            )

        mission.finished()

        return {
            "success": True
        }