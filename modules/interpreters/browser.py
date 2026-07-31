from core.browser_states import BrowserState
from core.interpretation import Interpretation

from modules.interpreters.base import Interpreter


class BrowserInterpreter(Interpreter):

    def interpret(
        self,
        observation
    ):
        text = " ".join(
            observation.visible_text
        ).lower()

        print("\n==============================")
        print("VISIBLE TEXT")
        print("==============================")
        print(text)
        print("==============================\n")
        state = BrowserState.UNKNOWN

        reason = "Unknown browser state."

        confidence = 0.50

        success = observation.success

        if observation.url:

            if "google.com/search" in observation.url:

                state = BrowserState.SEARCH_RESULTS

                reason = "Google search results detected."

                confidence = 0.98

            elif "google.com" in observation.url:

                state = BrowserState.GOOGLE_HOME

                reason = "Google homepage detected."

                confidence = 0.95

            elif "youtube.com" in observation.url:

                state = BrowserState.YOUTUBE_HOME

                reason = "YouTube page detected."

                confidence = 0.95

        return Interpretation(

            success=success,

            confidence=confidence,

            state=state,

            reason=reason,

            observation=observation

        )