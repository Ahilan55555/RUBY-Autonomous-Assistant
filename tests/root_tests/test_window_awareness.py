from modules.vision.window_context import (
    get_active_window
)

from modules.vision.window_analyzer import (
    analyze_window
)

window = get_active_window()

print(window)

if window["success"]:

    print(
        analyze_window(
            window["title"]
        )
    )