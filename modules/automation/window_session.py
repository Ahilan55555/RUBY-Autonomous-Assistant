from modules.automation.window_controller import (
    focus_window,
    get_active_window_id
)

import time


def focus_and_lock(title):

    result = focus_window(title)

    if not result["success"]:
        return result

    time.sleep(1)

    return get_active_window_id()