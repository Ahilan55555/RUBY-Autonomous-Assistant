from core.plan import Plan
from core.task_builder import TaskBuilder

from modules.agents.ui_agent import UIAgent


class BrowserSearchCapability:

    def __init__(self):

        self.tasks = TaskBuilder()

        self.ui = UIAgent()


    def build_plan(
        self,
        goal_context
    ):

        query = (

            goal_context.command

            .replace(

                "search google",

                ""

            )

            .strip()

        )

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