from core.action import Action
from core.action_queue import ActionQueue
from core.executor import Executor

queue = ActionQueue()

queue.add(

    Action(
        action="wait",
        seconds=1
    )

)

queue.add(

    Action(
        action="wait",
        seconds=1
    )

)

executor = Executor()

result = executor.execute_queue(
    queue
)

print(result)