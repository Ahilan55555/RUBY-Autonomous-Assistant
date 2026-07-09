class ActionQueue:

    def __init__(self):

        self.actions = []


    def add(
        self,
        action
    ):

        self.actions.append(
            action
        )


    def clear(
        self
    ):

        self.actions.clear()


    def __len__(
        self
    ):

        return len(
            self.actions
        )


    def __iter__(
        self
    ):

        return iter(
            self.actions
        )