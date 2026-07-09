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

from core.action import (
    Action
)

from core.action_queue import (
    ActionQueue
)

from core.executor import (
    Executor
)


class BrowserAgent:

    def __init__(
        self
    ):

        self.ui = UIAgent()

        self.executor = Executor()


    def search_google(
        self,
        query
    ):

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        open_google()

        self.ui.wait(
            3
        )

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        textbox = self.ui.find_best(
            app="Firefox",
            role="text_input"
        )

        if textbox is None:

            return {
                "success": False,
                "error": "Google search textbox not found"
            }

        queue = ActionQueue()

        queue.add(
            Action(
                action="click",
                target=textbox
            )
        )

        queue.add(
            Action(
                action="type",
                text=query
            )
        )

        queue.add(
            Action(
                action="wait",
                seconds=0.5
            )
        )

        queue.add(
            Action(
                action="press",
                key="enter"
            )
        )

        result = self.executor.execute_queue(
            queue
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

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        open_youtube()

        self.ui.wait(
            3
        )

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        textbox = self.ui.find_best(
            app="Firefox",
            role="text_input"
        )

        if textbox is None:

            return {
                "success": False,
                "error": "YouTube search textbox not found"
            }

        queue = ActionQueue()

        queue.add(
            Action(
                action="click",
                target=textbox
            )
        )

        queue.add(
            Action(
                action="type",
                text=query
            )
        )

        queue.add(
            Action(
                action="wait",
                seconds=0.5
            )
        )

        queue.add(
            Action(
                action="press",
                key="enter"
            )
        )

        result = self.executor.execute_queue(
            queue
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

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        open_chatgpt()

        self.ui.wait(
            5
        )

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        textbox = self.ui.find_best(
            app="Firefox",
            role="text_input"
        )

        if textbox is None:

            return {
                "success": False,
                "error": "ChatGPT textbox not found"
            }

        queue = ActionQueue()

        queue.add(
            Action(
                action="click",
                target=textbox
            )
        )

        queue.add(
            Action(
                action="type",
                text=prompt
            )
        )

        queue.add(
            Action(
                action="wait",
                seconds=0.5
            )
        )

        queue.add(
            Action(
                action="press",
                key="enter"
            )
        )

        result = self.executor.execute_queue(
            queue
        )

        if not result["success"]:
            return result

        return {
            "success": True,
            "prompt": prompt
        }


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