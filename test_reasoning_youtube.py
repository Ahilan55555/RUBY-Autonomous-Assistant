from modules.automation.accessibility import (
    get_ui_elements,
    find_application
)

app = find_application("Firefox")

elements = get_ui_elements(app)

for element in elements:

    if element["role"] == "document web":

        print("=" * 50)
        print("NAME :", element["name"])
        print("ROLE :", element["role"])
        print()

        print("STATES:")

        for state in element["states"]:
            print("   ", state)

        print()