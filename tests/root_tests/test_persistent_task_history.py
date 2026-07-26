from modules.memory.task_history import (
    TaskHistory
)

history = TaskHistory()

history.add(
    "Working on OCR"
)

history.add(
    "Improving Whisper"
)

history.add(
    "Developing AI Assistant"
)

print(
    history.recent()
)