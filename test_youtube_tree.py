from modules.automation.accessibility import (
    find_application,
    find_active_document,
    get_ui_elements
)

app = find_application("Firefox")

document = find_active_document(app)

elements = get_ui_elements(document)

print("TOTAL:", len(elements))

for element in elements:

    print("=" * 60)
    print("NAME :", repr(element["name"]))
    print("ROLE :", element["role"])
    print("BOUNDS :", element["bounds"])