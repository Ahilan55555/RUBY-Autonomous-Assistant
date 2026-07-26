from modules.memory.screen_context_memory import (
    ScreenContextMemory
)

memory = ScreenContextMemory()

memory.add(
    "Editing OCR code"
)

memory.add(
    "Running OCR tests"
)

memory.add(
    "Viewing OCR results"
)

print(
    memory.get_activity_chain()
)