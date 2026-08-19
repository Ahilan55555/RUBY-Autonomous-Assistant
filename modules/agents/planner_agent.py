from modules.agents.llm_planner import (
    LLMPlanner
)


class PlannerAgent:

    def __init__(self):

        self.planner = LLMPlanner()


    def plan(
        self,
        user_input
    ):

        return self.planner.plan(
            user_input
        )