class DecisionEngine:

    def decide(
        self,
        task,
        observation
    ):

        if observation["completed"]:

            return {

                "action": "continue"

            }

        return {

            "action": "abort"

        }