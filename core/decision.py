class Decision:

    def __init__(
        self,
        action="continue",
        reason=""
    ):

        self.action = action

        self.reason = reason

    def __repr__(self):

        return (
            f"Decision(action={self.action}, "
            f"reason={self.reason})"
        )