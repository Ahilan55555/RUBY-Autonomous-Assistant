from modules.memory.json_memory import (
    JsonMemory
)

memory = JsonMemory(
    "memory.json"
)

memory.save(
    {
        "project":
        "AI Assistant"
    }
)

print(
    memory.load()
)