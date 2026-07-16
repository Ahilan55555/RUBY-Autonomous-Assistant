from core.goal import Goal

from core.mission import Mission

from modules.capabilities.registry import CapabilityRegistry

from modules.agents.capability_selector import CapabilitySelector


class Planner:

    def __init__(self):
        self.registry = CapabilityRegistry()
        self.selector = CapabilitySelector()

    def interpret(
        self,
        text
    ):

        text = text.lower()

        if text.startswith("search google"):

            query = (

                text.replace(

                    "search google",

                    ""

                )

                .strip()

            )

            return Goal(

                action="search",

                target="google",

                data=query

            )

        return None


    def create_plan(
        self,
        mission_step,
        goal_context
    ):

        if mission_step == "search":

            return self.interpret(
                goal_context.command
            )

        return None

    def create_mission(
        self,
        command
    ):

        goal = self.interpret(
            command
        )

        mission = Mission(
            goal=command
        )

        return mission

    def build_plan(
        self,
        mission_step,
        goal_context
    ):

        capability_name = self.selector.choose(

            mission_step,

            goal_context

        )

        if capability_name is None:

            return None

        capability = self.registry.get(

            capability_name

        )

        if capability is None:

            return None

        return capability.build_plan(

            goal_context

        )