from modules.vision.window_capture import (
    capture_window
)

from modules.vision.ocr import (
    contains_text
)

capture_window(
    "Firefox"
)

print(
    contains_text(
        "temp/window_capture.png",
        "ChatGPT"
    )
)