from modules.perception.manager import (
    PerceptionManager
)

manager = PerceptionManager()

elements = manager.observe(
    "Firefox"
)

print(len(elements))

for element in elements[:20]:

    print(
        element["source"],
        element["role"],
        element["name"]
    )