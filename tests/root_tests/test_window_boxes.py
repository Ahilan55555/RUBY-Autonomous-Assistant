from modules.automation.window_controller import (
    get_active_window_id
)

from modules.vision.window_observer import (
    observe_window_boxes_by_id
)

window = get_active_window_id()

print(
    observe_window_boxes_by_id(
        window["window_id"]
    )
)