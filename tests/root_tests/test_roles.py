from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_all_role
)

app = find_application(
    "Firefox"
)

elements = get_ui_elements(
    app
)

for role in [
    "combo box",
    "entry",
    "text",
    "push button",
    "link",
    "document web"
]:

    print("\n==========", role, "==========")

    matches = find_all_role(
        elements,
        role
    )

    print("Found", len(matches))

    for match in matches[:10]:

        print(match["name"])