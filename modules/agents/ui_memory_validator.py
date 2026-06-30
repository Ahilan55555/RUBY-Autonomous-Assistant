from modules.memory.ui_memory import (
    get_ui_object,
    remember_ui_object
)


def validate_ui_object(
    app,
    name,
    visible_objects
):

    memory = get_ui_object(
        app,
        name
    )

    if not memory:

        return None

    if "text" not in memory:

        return None

    expected_text = (
        memory["text"]
        .lower()
    )

    for obj in visible_objects:

        if (
            expected_text
            in
            obj["text"].lower()
        ):

            remember_ui_object(
                app,
                name,
                obj
            )

            return obj

    return None