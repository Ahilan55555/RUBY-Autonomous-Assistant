from modules.memory.project_memory import (
    ProjectMemory
)

memory = ProjectMemory()

memory.add_fact(
    "AI Assistant",
    "Uses Whisper"
)

memory.add_fact(
    "AI Assistant",
    "Uses Piper"
)

memory.add_fact(
    "AI Assistant",
    "Desktop Awareness Module"
)

print(
    memory.get_project(
        "AI Assistant"
    )
)