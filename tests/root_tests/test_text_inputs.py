from modules.perception.manager import PerceptionManager

manager = PerceptionManager()

elements = manager.observe("Firefox")

count = 0

for element in elements:

    if element["role"] in (
        "entry",
        "combo box",
        "text",
        "editable text"
    ):

        count += 1

        print("=" * 60)
        print("TEXT INPUT", count)
        print("NAME :", repr(element["name"]))
        print("ROLE :", element["role"])
        print("BOUNDS :", element["bounds"])
        print()

print()
print("TOTAL:", count)