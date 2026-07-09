from modules.automation.accessibility import (
    find_application,
    find_active_document,
    get_ui_elements
)

app = find_application("Firefox")

doc = find_active_document(app)

elements = get_ui_elements(doc)

for element in elements:

    if element["bounds"] is None:
        continue

    if element["bounds"]["width"] < 40:
        continue

    if element["bounds"]["height"] < 20:
        continue

    print("=" * 40)
    print(element["role"])
    print(element["name"])
    print(element["bounds"])