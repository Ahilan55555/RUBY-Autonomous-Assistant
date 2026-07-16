from modules.agents.planner import Planner
from modules.agents.browser_agent import BrowserAgent
from modules.agents.mission_builder import MissionBuilder


class RubyAgent:

    def __init__(self):

        self.planner = Planner()

        self.browser = BrowserAgent()

        self.mission_builder = MissionBuilder()


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

    def create_mission(
        self,
        command
    ):

        return self.planner.create_mission(
            command
        )