from modules.agents.goal_executor import GoalExecutor


class MissionExecutor:

    def __init__(self):

        self.planner = Planner()

        self.browser = BrowserAgent()

        self.goal_executor = GoalExecutor()

    def run(
        self,
        mission
    ):

        for plan in mission.plans:

            result = self.goal_executor.run(
                plan
            )

            if not result["success"]:

                return result

        return {

            "success": True

        }