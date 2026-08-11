from core.plan import Plan
from core.task_builder import TaskBuilder
import time
from modules.agents.ui_agent import UIAgent
from modules.capabilities.base import Capability
from modules.perception.browser_observer import BrowserObserver
from modules.interpreters.browser import BrowserInterpreter
from modules.agents.decision_engine import DecisionEngine
from modules.agents.browser_navigation_agent import (
    BrowserNavigationAgent
)


class BrowserSearchCapability(Capability):

    def __init__(self):

        self.tasks = TaskBuilder()

        self.ui = UIAgent()

        self.navigator = BrowserNavigationAgent()

        self.observer = BrowserObserver()

        self.interpreter = BrowserInterpreter()

        self.decision_engine = DecisionEngine()

    def prepare(
        self,
        step,
        mission
    ):

        mission.context.set(
            "search_query",
            step.query
        )

    def build_plan(
        self,
        step,
        mission
    ):

        query = step.query

        print(
            ">>> BROWSER QUERY =",
            repr(query)
        )

        target = step.target



        print("\n===== ENSURE WEBSITE =====")

        if target == "search_google":
            self.navigator.open_google()

        elif target == "search_youtube":
            self.navigator.open_youtube()
            

        elif target == "ask_chatgpt":
            self.navigator.open_chatgpt()

        else:

            print(f"Unknown browser target: {target}")

            return None

        time.sleep(2)


        print("==========================\n")

        print("\n========== BROWSER TARGET ==========")
        print(target)
        print("===================================\n")

        if target == "search_google":

            textbox = self.ui.find_best(

                app="Firefox",

                role="text_input",

                text="search"

            )

        elif target == "search_youtube":

            textbox = self.ui.find_best(

                app="Firefox",

                role="text_input",

                text="search"

            )


        elif target == "ask_chatgpt":

            textbox = self.ui.find_best(
                app="Firefox",
                role="entry",
                text="Chat with ChatGPT"
            )

            if textbox is None:

                textbox = self.ui.find_best(
                    app="Firefox",
                    role="entry"
                )

            if textbox is None:

                textbox = self.ui.find_best(
                    app="Firefox",
                    role="text_input"
                )

        else:

            print(f"Unknown browser target: {target}")

            return None

        print("\n========== TEXTBOX ==========")
        print(textbox)
        print("=============================\n")

        if textbox is None:

            return None

        task = self.tasks.search(

            textbox,

            query

        )

        print("\n========== ACTION QUEUE ==========")

        for action in task.action_queue:
            print(action)

        print("===============================\n")

        goal_map = {

            "search_google": "Search Google",

            "search_youtube": "Search YouTube",

            "ask_chatgpt": "Ask ChatGPT"

        }

        plan = Plan(
            goal=goal_map.get(
                target,
                "Browser Action"
            )
        )

        plan.add_task(

            task

        )

        return plan

    

    def observe(self):

        return self.observer.observe()

    def apply_result(
        self,
        mission,
        decision
    ):

        return {

            "action": decision.action,

            "reason": decision.reason

        }

    def cleanup(
        self,
        mission
    ):

        pass

    def interpret(
        self,
        observation
    ):

        return self.interpreter.interpret(
            observation
        )

    def decide(
        self,
        interpretation,
        mission
    ):
        return self.decision_engine.decide(
            mission,
            interpretation
        )