from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_all_role
)

import pyatspi

app = find_application("Firefox")

elements = get_ui_elements(app)

entry = find_all_role(
    elements,
    "entry"
)[0]

node = entry["node"]

component = node.queryComponent()

rect = component.getExtents(
    pyatspi.XY_SCREEN
)

print(rect.x)
print(rect.y)
print(rect.width)
print(rect.height)