from core.plan import Plan
from core.task_builder import TaskBuilder

from modules.agents.ui_agent import UIAgent
from modules.capabilities.base import Capability


class BrowserSearchCapability(Capability):

    def __init__(self):

        self.tasks = TaskBuilder()

        self.ui = UIAgent()

    def prepare(
        self,
        step,
        mission
    ):

        mission.context.set(
            "search_query",
            step.target
        )

    def build_plan(
        self,
        step,
        mission
    ):

        query = step.target

        textbox = self.ui.find_best(

            app="Firefox",

            role="text_input"

        )

        if textbox is None:

            return None

        task = self.tasks.search(

            textbox,

            query

        )

        plan = Plan(

            goal="Search Google"

        )

        plan.add_task(

            task

        )

        return plan

    def collect_result(
        self,
        mission,
        observation
    ):

        return observation

    def cleanup(
        self,
        mission
    ):

        pass