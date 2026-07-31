class Interpretation:

    def __init__(
        self,
        success=False,
        confidence=0.0,
        state="",
        reason="",
        observation=None
    ):

        self.success = success
        self.confidence = confidence
        self.state = state
        self.reason = reason
        self.observation = observation