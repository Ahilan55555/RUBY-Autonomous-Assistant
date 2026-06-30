from modules.automation.window_controller import (
    get_active_window_id,
    get_window_rect_by_id
)

window = get_active_window_id()

print(
    get_window_rect_by_id(
        window["window_id"]
    )
)