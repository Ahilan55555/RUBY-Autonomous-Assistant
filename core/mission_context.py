class MissionContext:

    def __init__(self):

        self.data = {}

    def set(
        self,
        key,
        value
    ):

        self.data[key] = value

    def get(
        self,
        key,
        default=None
    ):

        return self.data.get(
            key,
            default
        )

    def has(
        self,
        key
    ):

        return key in self.data

    def clear(self):

        self.data.clear()

    def __repr__(self):

        return f"MissionContext({self.data})"