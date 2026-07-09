class Task:

    def __init__(
        self,
        name,
        action_queue=None,
        parameters=None
    ):

        self.name = name

        self.action_queue = action_queue

        self.parameters = parameters or {}

    def __repr__(self):

        return (

            f"Task("

            f"name={self.name}, "

            f"parameters={self.parameters}"

            f")"

        )