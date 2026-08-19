from core.plan import Plan
from core.task import Task
from core.action import Action
from core.action_queue import ActionQueue
from core.world_state import get_state
from modules.capabilities.base import Capability
from modules.automation.mouse_controller import scroll
from modules.perception.manager import PerceptionManager
from modules.automation.screen_actions import (
    click_text,
    double_click_text,
    right_click_text,
    type_at_text
)


class ScreenCapability(Capability):

    def __init__(self):
        self.perception = PerceptionManager()
        self.last_execution = None

    def prepare(
        self,
        step,
        mission
    ):
        pass


    def build_plan(
        self,
        step,
        mission
    ):

        target = step.target

        # ---------------------------------
        # SCROLL
        # ---------------------------------

        if target == "scroll":

            direction = (
                step.query
                .lower()
                .strip()
            )

            if direction == "down":

                amount = -5

            elif direction == "up":

                amount = 5

            else:

                try:

                    amount = int(direction)

                except ValueError:

                    return None

            queue = ActionQueue()

            queue.add(
                Action(
                    action="scroll",
                    amount=amount
                )
            )

            task = Task(
                name="Scroll",
                action_queue=queue
            )

            plan = Plan(
                goal="Scroll screen"
            )

            plan.add_task(
                task
            )

            return plan


        # ---------------------------------
        # CLICK TEXT
        # ---------------------------------

        if target == "click_text":

            text = (
                step.query
                .strip()
            )

            if not text:
                return None

            task = Task(
                name="Click Text",
                capability="screen.click_text",
                parameters={
                    "text": text,
                    "app": getattr(
                        mission,
                        "app",
                        None
                    )
                }
            )

            plan = Plan(
                goal=f"Click '{text}'"
            )

            plan.add_task(
                task
            )

            return plan


        # ---------------------------------
        # DOUBLE CLICK TEXT
        # ---------------------------------

        if target == "double_click_text":

            text = (
                step.query
                .strip()
            )

            if not text:
                return None

            task = Task(
                name="Double Click Text",
                capability="screen.double_click_text",
                parameters={
                    "text": text
                }
            )

            plan = Plan(
                goal=f"Double click '{text}'"
            )

            plan.add_task(
                task
            )

            return plan


        # ---------------------------------
        # RIGHT CLICK TEXT
        # ---------------------------------

        if target == "right_click_text":

            text = (
                step.query
                .strip()
            )

            if not text:
                return None

            task = Task(
                name="Right Click Text",
                capability="screen.right_click_text",
                parameters={
                    "text": text
                }
            )

            plan = Plan(
                goal=f"Right click '{text}'"
            )

            plan.add_task(
                task
            )

            return plan


        # ---------------------------------
        # TYPE AT TEXT
        # ---------------------------------

        if target == "type_at_text":

            # Expected format:
            #
            # "textbox | text to type"
            #

            if "|" not in step.query:
                return None

            text_to_find, text_to_type = (
                step.query.split(
                    "|",
                    1
                )
            )

            text_to_find = text_to_find.strip()
            text_to_type = text_to_type.strip()

            if not text_to_find:
                return None

            task = Task(
                name="Type At Text",
                capability="screen.type_at_text",
                parameters={
                    "text_to_find": text_to_find,
                    "text_to_type": text_to_type
                }
            )

            plan = Plan(
                goal=f"Type into '{text_to_find}'"
            )

            plan.add_task(
                task
            )

            return plan


        return None


    def execute(
        self,
        task,
        mission
    ):

        capability = task.capability

        parameters = task.parameters

        # ---------------------------------
        # SCROLL
        # ---------------------------------

        if capability == "screen.scroll":

            return scroll(
                parameters.get(
                    "amount"
                )
            )


        # ---------------------------------
        # CLICK TEXT
        # ---------------------------------

        if capability == "screen.click_text":

            return click_text(
                parameters.get(
                    "text"
                )
            )


        # ---------------------------------
        # DOUBLE CLICK TEXT
        # ---------------------------------

        if capability == "screen.double_click_text":

            return double_click_text(
                parameters.get(
                    "text"
                )
            )


        # ---------------------------------
        # RIGHT CLICK TEXT
        # ---------------------------------

        if capability == "screen.right_click_text":

            return right_click_text(
                parameters.get(
                    "text"
                )
            )


        # ---------------------------------
        # TYPE AT TEXT
        # ---------------------------------

        if capability == "screen.type_at_text":

            return type_at_text(
                parameters.get(
                    "text_to_find"
                ),
                parameters.get(
                    "text_to_type"
                )
            )


        return {
            "success": False,
            "error": (
                f"Unknown screen capability: "
                f"{capability}"
            )
        }


    def observe(self):

        state = get_state()

        app_name = state.get(
            "active_app"
        )

        if not app_name:

            print(
                "[Screen Capability] "
                "No active application in world state."
            )

            return None

        print(
            "[Screen Capability] "
            f"Observing application: {app_name}"
        )

        observation = self.perception.observe(
            app_name
        )

        return observation

    def interpret(
        self,
        observation
    ):

        return observation


    def decide(
        self,
        interpretation,
        mission
    ):

        class Decision:

            action = "continue"

            reason = "Screen action completed."

        return Decision()


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