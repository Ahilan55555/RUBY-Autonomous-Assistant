from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_first_name
)

app = find_application(
    "Firefox"
)

elements = get_ui_elements(
    app
)

search = find_first_name(
    elements,
    "Search"
)

print(search)