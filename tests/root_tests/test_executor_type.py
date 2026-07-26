from core.executor import Executor
from core.action import Action

executor = Executor()

result = executor.execute(

    Action(

        action="type",

        text="Hello Ruby"

    )

)

print(result)