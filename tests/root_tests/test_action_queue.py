from core.action import Action
from core.action_queue import ActionQueue

queue = ActionQueue()

queue.add(
    Action(
        action="click",
        target="Search Box"
    )
)

queue.add(
    Action(
        action="type",
        text="robotics"
    )
)

queue.add(
    Action(
        action="press",
        key="enter"
    )
)

print(len(queue))

for action in queue:

    print(action)