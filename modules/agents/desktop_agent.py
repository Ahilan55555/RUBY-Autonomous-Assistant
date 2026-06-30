from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

from core.intent_executor import (
    execute_intent
)

from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.window_capture import (
    capture_window,
    capture_window_by_id
)

from modules.vision.ocr import (
    read_screen_text
)

from modules.agents.verification_agent import (
    VerificationAgent
)

from modules.vision.window_observer import (
    observe_window,
    observe_active_window,
    observe_window_boxes_by_id
)

from modules.automation.window_controller import (
    get_active_window_id
)

import time


class DesktopAgent:

    def __init__(self):

        self.planner = AdaptivePlanner()

        self.verifier = VerificationAgent()

        self.target_window_id = None

    def observe(self):

        return observe_active_window()

    def run(self, goal):

        plan = self.planner.recover(
            goal
        )

        print(
            "\n===== PLAN ====="
        )

        print(
            plan.tasks
        )

        print(
            "================\n"
        )

        results = []

        for task in plan.tasks:

            result = execute_intent(
                {
                    "intent": task.intent,
                    "target": task.target,
                    "query": task.query
                }
            )
            if (
                task.intent == "window"
                and
                task.target == "focus"
            ):
                self.lock_active_window()

            if (
                task.intent == "open_app"
                and
                task.target == "firefox"
            ):
                self.lock_active_window()

            print(
                "\n===== RESULT ====="
            )

            print(
                result
            )

            print(
                "=================="
            )

            results.append(
                result
            )

            screen_text = (
                self.observe_locked_window()
            )

            print(
                "\n===== OBSERVATION ====="
            )

            print(
                screen_text[:1000]
            )

            print(
                "=======================\n"
            )

        return results

    def verify_text(
        self,
        expected_text,
        timeout=10
    ):

        import time

        for _ in range(timeout):

            visible = (
                self.observe_locked_window_boxes()
            )

            if self.verifier.text_exists(
                expected_text,
                visible
            ):
                return True

            time.sleep(1)

        return False
            
    def run_and_verify(
        self,
        goal,
        expected_text
    ):

        results = self.run(goal)

        execution_success = all(
            result.get("success", False)
            for result in results
        )

        verification_success = (
            self.verify_text(
                expected_text
            )
        )

        return {
            "success":
                execution_success
                and
                verification_success,

            "results": results
        }

        
    def observe_focused_window(
        self,
        window_id
    ):

        result = capture_window_by_id(
            window_id,
            "temp/focused_window.png"
        )

        if not result["success"]:
            return ""

        return read_screen_text(
            result["path"]
        )

    def lock_active_window(self):

        time.sleep(1)

        result = get_active_window_id()

        if result["success"]:

            self.target_window_id = (
                result["window_id"]
            )

            print(
                "LOCKED:",
                self.target_window_id
            )

        return result
        
    def observe_window(
        self,
        title
    ):

        return observe_window(
            title
            )


    def observe_locked_window(self):

        if not self.target_window_id:

            return ""

        result = capture_window_by_id(
            self.target_window_id,
            "temp/locked_window.png"
        )

        if not result["success"]:

            return ""

        return read_screen_text(
            result["path"]
        )

    def observe_locked_window_boxes(
        self
    ):

        if not self.target_window_id:

            return []

        return observe_window_boxes_by_id(
            self.target_window_id
        )

    def observe_locked_window_objects(
        self
    ):

        return self.observe_locked_window_boxes()


    def focus_and_lock_window(
        self,
        title
    ):

        execute_intent(
            {
                "intent": "window",
                "target": "focus",
                "query": title
            }
        )

        time.sleep(1)

        return self.lock_active_window()