from modules.perception.manager import (
    PerceptionManager
)

manager = PerceptionManager()

elements = manager.observe(
    "Firefox"
)

print(elements[0])