import json
import os

from dataclasses import is_dataclass, asdict


STATE_FILE = "data/world_state.json"


def default_state():
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


def load_state():

    if not os.path.exists(STATE_FILE):
        return default_state()

    try:

        with open(STATE_FILE, "r") as file:
            state = json.load(file)

        # Make sure old/incomplete state files
        # receive any newly introduced fields.
        default = default_state()

        for key, value in default.items():

            if key not in state:
                state[key] = value

        return state

    except json.JSONDecodeError:

        print("[World State] Invalid JSON. Resetting state.")

        return default_state()

    except OSError as e:

        print(f"[World State] Could not read state: {e}")

        return default_state()


world_state = load_state()


def save_state():

    os.makedirs(
        os.path.dirname(STATE_FILE),
        exist_ok=True
    )

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