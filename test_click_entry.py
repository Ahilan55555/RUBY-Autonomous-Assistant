from modules.automation.accessibility import (
    find_first_editable_entry
)

from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

entry = find_first_editable_entry(
    "Firefox"
)

print(entry)

bounds = entry["bounds"]

x = bounds["x"] + bounds["width"] // 2
y = bounds["y"] + bounds["height"] // 2

move_mouse(
    x,
    y
)

left_click()

print("Clicked")