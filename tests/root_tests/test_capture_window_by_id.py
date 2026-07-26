from modules.automation.window_controller import (
    get_active_window_id
)

from modules.vision.window_capture import (
    capture_window_by_id
)

from modules.vision.ocr import (
    read_screen_text
)

window = get_active_window_id()

print(window)

capture = capture_window_by_id(
    window["window_id"]
)

print(capture)

print(
    read_screen_text(
        capture["path"]
    )
)