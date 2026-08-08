import json

from dataclasses import is_dataclass, asdict

STATE_FILE = (
    "data/world_state.json"
)


def load_state():

    try:

        with open(
            STATE_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return {

            # -----------------------------
            # Application State
            # -----------------------------

            "active_app": None,
            "active_window": None,

            # -----------------------------
            # Browser State
            # -----------------------------

            "current_website": None,
            "current_url": None,
            "current_page": None,

            # -----------------------------
            # Workspace
            # -----------------------------

            "working_directory": None,

            # -----------------------------
            # Task History
            # -----------------------------

            "last_goal": None,
            "last_task": None,
            "last_action": None,
            "last_result": None,
            "last_search": None,

            # -----------------------------
            # Screen
            # -----------------------------

            "screen_context": None
        }


world_state = load_state()


def save_state():

    with open(
        STATE_FILE,
        "w"
    ) as file:

        json.dump(
            world_state,
            file,
            indent=4
        )


def update_state(
    key,
    value
):

    if is_dataclass(value):

        value = asdict(value)

    world_state[key] = value

    save_state()


def get_state():

    return world_state