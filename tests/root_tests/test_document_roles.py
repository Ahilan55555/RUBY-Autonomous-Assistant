from collections import Counter

from modules.automation.accessibility import (
    find_application,
    find_active_document,
    get_ui_elements
)

app = find_application("Firefox")
doc = find_active_document(app)

elements = get_ui_elements(doc)

roles = Counter()

for element in elements:

    roles[element["role"]] += 1

for role, count in sorted(roles.items()):

    print(f"{role:20} {count}")