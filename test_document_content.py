from modules.automation.accessibility import (
    find_application,
    find_active_document,
    get_ui_elements
)

app = find_application("Firefox")
doc = find_active_document(app)

elements = get_ui_elements(doc)

for element in elements:

    role = element["role"]

    if role not in (
        "paragraph",
        "static",
        "heading"
    ):
        continue

    name = element["name"].strip()

    if not name:
        continue

    print("=" * 60)
    print("ROLE :", role)
    print("TEXT :", repr(name))