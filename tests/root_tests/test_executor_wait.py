from core.executor import Executor
from core.action import Action

executor = Executor()

print("Waiting...")

result = executor.execute(

    Action(

        action="wait",

        seconds=2

    )

)

print(result)