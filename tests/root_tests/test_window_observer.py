from modules.vision.window_observer import (
    observe_window
)

texts = observe_window(
    "Firefox"
)

for text in texts:

    print(text)