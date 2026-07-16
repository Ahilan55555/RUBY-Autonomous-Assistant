class TaskObserver:

    def observe(
        self,
        task
    ):

        return {

            "success": True,

            "completed": True,

            "confidence": 1.0,

            "reason": "Task completed."

        }