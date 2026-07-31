import json

from datetime import datetime

from dataclasses import asdict, is_dataclass


HISTORY_FILE = (
    "data/execution_history.json"
)


def load_history():

    try:

        with open(
            HISTORY_FILE,
            "r"
        ) as file:

            return json.load(file)

    except:

        return []


def save_history(history):

    with open(
        HISTORY_FILE,
        "w"
    ) as file:

        json.dump(
            history,
            file,
            indent=4
        )


def record_execution(

    task,

    result
):

    history = load_history()

    if is_dataclass(task):

        task = asdict(task)

    history.append(
        {
            "timestamp": str(
                datetime.now()
            ),

            "task": task,

            "result": result
        }
    )
    save_history(history)