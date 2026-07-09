class Goal:

    def __init__(
        self,
        action,
        target=None,
        data=None
    ):

        self.action = action

        self.target = target

        self.data = data

    def __repr__(self):

        return (

            f"Goal(action={self.action}, "

            f"target={self.target}, "

            f"data={self.data})"

        )