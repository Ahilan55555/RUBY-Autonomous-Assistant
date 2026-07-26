from core.action_executor import (
    ActionExecutor
)

executor = ActionExecutor()

print(
    executor.execute(
        [
            "open_github"
        ]
    )
)