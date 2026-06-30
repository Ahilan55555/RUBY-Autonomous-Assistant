from modules.memory.ui_memory import (
    remember_ui_object,
    get_ui_object
)

remember_ui_object(

    "chatgpt",

    "textbox",

    {
        "x": 1212,
        "y": 573
    }
)

print(
    get_ui_object(
        "chatgpt",
        "textbox"
    )
)