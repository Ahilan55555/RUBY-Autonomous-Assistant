from modules.vision.window_capture import (
    capture_active_window
)

from modules.vision.ocr import (
    get_visible_texts
)

capture_active_window()

texts = get_visible_texts(
    "temp/active_window.png"
)

for text in texts:
    print(repr(text))