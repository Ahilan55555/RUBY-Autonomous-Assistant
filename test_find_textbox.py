from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_first_role
)

app = find_application(
    "Firefox"
)

elements = get_ui_elements(
    app
)

textbox = find_first_role(
    elements,
    "combo box"
)

print(textbox)