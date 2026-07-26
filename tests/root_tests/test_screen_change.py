from modules.agents.screen_change_detector import (
    ScreenChangeDetector
)

detector = (
    ScreenChangeDetector()
)

print(
    detector.has_changed(
        "screen.png"
    )
)

print(
    detector.has_changed(
        "screen.png"
    )
)