from core.browser_states import BrowserState
from core.decision import Decision


class DecisionEngine:

    def decide(
        self,
        task,
        interpretation
    ):

        if not interpretation.success:

            return Decision(
                action="abort",
                reason=interpretation.reason
            )

        if interpretation.state == BrowserState.PAGE_LOADING:

            return Decision(
                action="wait",
                reason="Page is still loading."
            )

        if interpretation.state == BrowserState.CAPTCHA:

            return Decision(
                action="request_user",
                reason="CAPTCHA detected."
            )

        if interpretation.state == BrowserState.ERROR_PAGE:

            return Decision(
                action="retry",
                reason="Browser error detected."
            )

        return Decision(
            action="continue",
            reason=interpretation.reason
        )