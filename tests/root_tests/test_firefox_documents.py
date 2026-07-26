from modules.automation.accessibility import (
    get_ui_elements,
    find_application
)

app = find_application("Firefox")

elements = get_ui_elements(app)

print("Documents:\n")

for e in elements:

    if e["role"] == "document web":

        print(e["name"])