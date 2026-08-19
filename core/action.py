class Action:

    def __init__(
        self,
        action,
        target=None,
        text=None,
        key=None,
        keys=None,
        seconds=None,
        amount=None
    ):

        self.action = action
        self.target = target
        self.text = text
        self.key = key
        self.keys = keys
        self.seconds = seconds
        self.amount = amount

        
    def __repr__(self):

        return (
            f"Action("
            f"action={self.action}, "
            f"target={self.target}, "
            f"text={self.text}, "
            f"key={self.key}, "
            f"keys={self.keys}, "
            f"seconds={self.seconds}, "
            f"amount={self.amount}"
            f")"
        )