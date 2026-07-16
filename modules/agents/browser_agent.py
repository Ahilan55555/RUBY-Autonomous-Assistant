from modules.automation.browser import (
    open_google,
    open_youtube,
    open_chatgpt
)

from modules.automation.window_session import (
    focus_and_lock
)

from modules.agents.ui_agent import (
    UIAgent
)

from core.task_builder import TaskBuilder

from core.plan import Plan

from modules.agents.goal_executor import GoalExecutor


class BrowserAgent:

    def __init__(
        self
    ):

        self.ui = UIAgent()

        self.task_builder = TaskBuilder()

        self.goal_executor = GoalExecutor()

    def search_google_plan(
        self,
        query
    ):

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return None

        open_google()

        self.ui.wait(
            3
        )

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return None

        textbox = self.ui.find_best(
            app="Firefox",
            role="text_input"
        )

        if textbox is None:
            return None

        task = self.task_builder.search(
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


    def search_youtube_plan(
        self,
        query
    ):

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return None

        open_youtube()

        self.ui.wait(
            3
        )

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return None

        textbox = self.ui.find_best(
            app="Firefox",
            role="text_input"
        )

        if textbox is None:
            return None

        task = self.task_builder.search(
            textbox,
            query
        )

        plan = Plan(
            goal="Search YouTube"
        )

        plan.add_task(
            task
        )

        return plan

    def ask_chatgpt_plan(
        self,
        prompt
    ):

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return None

        open_chatgpt()

        self.ui.wait(
            5
        )

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return None

        textbox = self.ui.find_best(
            app="Firefox",
            role="text_input"
        )

        if textbox is None:
            return None

        task = self.task_builder.search(
            textbox,
            prompt
        )

        plan = Plan(
            goal="Ask ChatGPT"
        )

        plan.add_task(
            task
        )

        return plan


    def search_google(
            self,
            query
        ):

            plan = self.search_google_plan(
                query
            )

            if plan is None:

                return {

                    "success": False,

                    "error": "Could not create plan"

                }

            result = self.goal_executor.run(
                plan
            )

            if not result["success"]:
                return result

            return {

                "success": True,

                "query": query

            }    


    def search_youtube(
        self,
        query
    ):

        plan = self.search_youtube_plan(
            query
        )

        if plan is None:

            return {

                "success": False,

                "error": "Could not create plan"

            }

        result = self.goal_executor.run(
            plan
        )

        if not result["success"]:
            return result

        return {

            "success": True,

            "query": query

        }

    def ask_chatgpt(
        self,
        prompt
    ):

        plan = self.ask_chatgpt_plan(
            prompt
        )

        if plan is None:

            return {

                "success": False,

                "error": "Could not create plan"

            }

        result = self.goal_executor.run(
            plan
        )

        if not result["success"]:
            return result

        return {

            "success": True,

            "prompt": prompt

        }
    def goal_to_plan(
        self,
        goal
    ):

        if goal.action == "search":

            if goal.target == "google":

                return self.search_google_plan(
                    goal.data
                )

            if goal.target == "youtube":

                return self.search_youtube_plan(
                    goal.data
                )

        if goal.action == "ask":

            if goal.target == "chatgpt":

                return self.ask_chatgpt_plan(
                    goal.data
                )

        return None


    def execute_goal(
        self,
        goal
    ):

        if goal.action == "search":

            if goal.target == "google":

                return self.search_google(
                    goal.data
                )

            if goal.target == "youtube":

                return self.search_youtube(
                    goal.data
                )

        if goal.action == "ask":

            if goal.target == "chatgpt":

                return self.ask_chatgpt(
                    goal.data
                )

        return {

            "success": False,

            "error": f"Unknown goal: {goal}"

        }