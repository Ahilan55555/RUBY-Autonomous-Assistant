from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_elements_by_name
)

app = find_application(
    "Firefox"
)

if app is None:
    print("Firefox not found")
    exit()

elements = get_ui_elements(app)

matches = find_elements_by_name(
    elements,
    "Search"
)

print(f"Found {len(matches)} matches\n")

for match in matches:
    print(match)