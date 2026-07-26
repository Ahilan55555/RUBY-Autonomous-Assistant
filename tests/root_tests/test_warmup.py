import time

from modules.llm.ollama_client import ask_llm

for i in range(5):

    start = time.time()

    ask_llm("hi")

    print(
        f"RUN {i+1}:",
        time.time() - start
    )