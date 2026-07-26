class MissionStep:

    def __init__(
        self,
        action,
        target=None,
        parameters=None
    ):

        self.action = action

        self.target = target

        self.parameters = parameters or {}

        self.status = "pending"

        self.result = None

        self.retry_count = 0

    def completed(
        self,
        result=None
    ):

        self.status = "completed"

        self.result = result

    def failed(self):

        self.status = "failed"

    def __repr__(self):

        return (

            f"MissionStep("
            f"action={self.action}, "
            f"target={self.target}, "
            f"status={self.status}, "
            f"result={self.result}"
            f")"

        )