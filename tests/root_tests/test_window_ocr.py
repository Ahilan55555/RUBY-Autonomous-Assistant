from modules.vision.window_capture import (
    capture_window
)

from modules.vision.ocr import (
    read_screen_text
)

capture_window(
    "Firefox"
)

text = read_screen_text(
    "temp/window_capture.png"
)

print(text)