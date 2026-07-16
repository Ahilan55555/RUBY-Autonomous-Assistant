from modules.agents.task_observer import TaskObserver

from core.task import Task

observer = TaskObserver()

task = Task(
    name="Search"
)

result = observer.observe(
    task
)

print(result)