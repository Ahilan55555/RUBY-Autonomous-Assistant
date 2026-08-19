from modules.agents.ui_agent import (
    UIAgent
)

from modules.agents.verification_agent import (
    VerificationAgent
)

from modules.automation.mouse_controller import scroll

class Executor:

    def __init__(
        self
    ):

        self.ui = UIAgent()

        self.verifier = VerificationAgent()


    def execute(
        self,
        action
    ):

        if action.action == "click":

            result = self.ui.click(
                action.target
            )

            if not result["success"]:
                return result

            return {
                "success": True,
                "action": "click_executed"
            }


        elif action.action == "double_click":

            return self.ui.double_click(
                action.target
            )


        elif action.action == "right_click":

            return self.ui.right_click(
                action.target
            )


        elif action.action == "hover":

            return self.ui.hover(
                action.target
            )


        elif action.action == "type":

            result = self.ui.type(
                action.text
            )

            if not result["success"]:
                return result

            return {
                "success": True
            }


        elif action.action == "press":

            return self.ui.press(
                action.key
            )
        elif action.action == "hotkey":

            return self.ui.hotkey(
                action.keys
            )


        elif action.action == "wait":

            return self.ui.wait(
                action.seconds
            )

        elif action.action == "scroll":

            return scroll(
                action.amount
            )


        return {
            "success": False,
            "error": f"Unknown action: {action.action}"
        }


    def execute_queue(
        self,
        queue
    ):

        results = []

        for action in queue:

            result = self.execute(
                action
            )

            results.append(
                result
            )

            if not result["success"]:

                return {
                    "success": False,
                    "results": results
                }

        return {
            "success": True,
            "results": results
        }