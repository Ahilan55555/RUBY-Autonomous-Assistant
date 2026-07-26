from modules.vision.screen_capture import (
    capture_screen
)

path = capture_screen()

print(
    f"Saved: {path}"
)