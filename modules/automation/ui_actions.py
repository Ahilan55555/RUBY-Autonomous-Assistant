from modules.memory.ui_memory import (
    get_ui_object
)

from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)


def click_ui_object(
    app,
    name
):

    obj = get_ui_object(
        app,
        name
    )

    if not obj:

        return {
            "success": False
        }

    move_mouse(
        obj["x"],
        obj["y"]
    )

    left_click()

    return {
        "success": True
    }