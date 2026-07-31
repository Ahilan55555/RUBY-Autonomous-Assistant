from core.plan import Plan
from core.task_builder import TaskBuilder

from modules.agents.ui_agent import UIAgent
from modules.capabilities.base import Capability
from modules.perception.browser_observer import BrowserObserver
from modules.interpreters.browser import BrowserInterpreter
from modules.agents.decision_engine import DecisionEngine


class BrowserSearchCapability(Capability):

    def __init__(self):

        self.tasks = TaskBuilder()

        self.ui = UIAgent()

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


    def observe(self):

        return self.observer.observe()

    def apply_result(
        self,
        mission,
        decision
    ):

        return decision

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