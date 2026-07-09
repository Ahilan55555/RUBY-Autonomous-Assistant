from modules.agents.planner import Planner
from modules.agents.browser_agent import BrowserAgent


class RubyAgent:

    def __init__(self):

        self.planner = Planner()

        self.browser = BrowserAgent()


    def execute(
        self,
        command
    ):

        goal = self.planner.interpret(
            command
        )

        if goal is None:

            return {

                "success": False,

                "error": "Could not understand command"

            }

        return self.browser.execute_goal(
            goal
        )