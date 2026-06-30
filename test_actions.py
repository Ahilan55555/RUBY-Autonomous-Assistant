from modules.automation.accessibility import (
    find_application,
    get_ui_elements,
    find_all_role
)

app = find_application("Firefox")

elements = get_ui_elements(app)

entries = find_all_role(
    elements,
    "entry"
)

entry = entries[0]

node = entry["node"]

try:
    action = node.queryAction()

    print("Actions:", action.nActions)

    for i in range(action.nActions):
        print(
            i,
            action.getName(i)
        )

except Exception as e:
    print(e)