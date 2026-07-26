from modules.llm.ollama_client import ask_llm
import time

start = time.time()

print(
    ask_llm(
        "hi"
    )
)

print(
    "TIME:",
    time.time() - start
)