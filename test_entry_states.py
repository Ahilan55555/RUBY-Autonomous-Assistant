from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_all_role
)

app = find_application(
    "Firefox"
)

elements = get_ui_elements(app)

entries = find_all_role(
    elements,
    "entry"
)

for entry in entries:

    print(entry["name"])
    print(entry["states"])
    print("-" * 50)