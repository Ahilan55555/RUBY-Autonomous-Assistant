from core.task_builder import TaskBuilder

builder = TaskBuilder()

task = builder.search(

    "Search Box",

    "robotics"

)

print(task)
print(task.action_queue)