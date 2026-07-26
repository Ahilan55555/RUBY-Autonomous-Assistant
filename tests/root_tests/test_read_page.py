from modules.perception.manager import PerceptionManager

manager = PerceptionManager()

elements = manager.observe_page(
    "Firefox"
)

print("TOTAL:", len(elements))

for element in elements[:50]:

    if element["name"]:

        print(
            element["role"],
            "->",
            element["name"]
        )