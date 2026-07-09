from core.task_builder import TaskBuilder

builder = TaskBuilder()

print(

    builder.type(
        "Hello"
    )

)

print(

    builder.press(
        "enter"
    )

)

print(

    builder.wait(
        1
    )

)