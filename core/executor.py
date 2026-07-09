from modules.agents.ui_agent import (
    UIAgent
)

from modules.agents.verification_agent import (
    VerificationAgent
)


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

            if not self.verifier.verify_exists(
                action.target
            ):

                return {
                    "success": False,
                    "error": "Verification failed"
                }

            return {
                "success": True
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


        elif action.action == "wait":

            return self.ui.wait(
                action.seconds
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