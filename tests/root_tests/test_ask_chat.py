import time

from modules.llm.chat_client import (
    ask_chat
)

start = time.time()

print(
    ask_chat("hi")
)

print(
    "\nTIME:",
    time.time() - start
)