import json
import os

MEMORY_FILE = (
    "data/ui_memory.json"
)

def load_ui_memory():

    if not os.path.exists(
        MEMORY_FILE
    ):

        return {}

    with open(
        MEMORY_FILE,
        "r"
    ) as f:

        return json.load(f)


def save_ui_memory(data):

    with open(
        MEMORY_FILE,
        "w"
    ) as f:

        json.dump(
            data,
            f,
            indent=4
        )


def remember_ui_object(
    app,
    name,
    obj
):

    memory = load_ui_memory()

    if app not in memory:

        memory[app] = {}

    memory[app][name] = obj

    save_ui_memory(memory)


def get_ui_object(
    app,
    name
):

    memory = load_ui_memory()

    return (
        memory
        .get(app, {})
        .get(name)
    )