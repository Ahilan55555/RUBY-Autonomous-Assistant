from modules.agents.desktop_agent import (
    DesktopAgent
)

from modules.vision.window_capture import (
    capture_active_window
)

from modules.vision.ocr import (
    get_visible_texts,
    find_similar_text
)

class AutonomousAgent:

    def __init__(self):

        self.desktop = DesktopAgent()

    
    def run_goal(
        self,
        goal,
        expected_text,
        max_attempts=3
    ):
        current_goal = goal
        
        for attempt in range(
            max_attempts
        ):

            print(
                f"\n===== ATTEMPT {attempt + 1} ====="
            )

            result = (
                self.desktop.run_and_verify(
                    current_goal,
                    expected_text
                )
            )

            print(
                "\nVERIFY RESULT:",
                result
            )

            if result["success"]:

                return {
                    "success": True,
                    "attempts": attempt + 1
                }

            diagnosis = self.diagnose_failure(
                expected_text
            )

            print(
                "\nDIAGNOSIS:",
                diagnosis
            )

            current_goal = (
                self.create_repair_goal(
                    current_goal,
                    expected_text
                )
            )

            print(
                "\nREPAIRED GOAL:",
                current_goal
            )

            
        return {
            "success": False,
            "attempts": max_attempts
        }

    def repair_target(
        self,
        expected_text
    ):

        visible = (
            self.desktop
            .observe_locked_window_boxes()
        )

        print(
            "\nVISIBLE TEXTS:"
        )

        for text in visible:
            print(repr(text))

        repair = find_similar_text(
            expected_text,
            visible
        )

        return repair

    def create_repair_goal(
        self,
        goal,
        expected_text
    ):

        repair = self.repair_target(
            expected_text
        )

        if repair:

            return goal.replace(
                expected_text,
                repair
            )

        return goal

    def diagnose_failure(
        self,
        expected_text
    ):

        visible = (
            self.desktop
            .observe_locked_window_boxes()
        )

        return {

            "expected":
                expected_text,

            "visible":
                visible[:20]
        }