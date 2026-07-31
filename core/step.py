class Step:

    def __init__(
        self,
        intent,
        target=None,
        query=None,
        parameters=None
    ):

        self.intent = intent

        self.target = target

        self.query = query

        self.parameters = parameters or {}

    def __repr__(self):

        return (

            f"Step("

            f"intent={self.intent}, "

            f"target={self.target}, "

            f"query={self.query}, "

            f"parameters={self.parameters}"

            f")"

        )