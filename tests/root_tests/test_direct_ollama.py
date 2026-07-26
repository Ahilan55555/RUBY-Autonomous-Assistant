import requests
import time

start = time.time()

response = requests.post(

    "http://localhost:11434/api/generate",

    json={
        "model": "qwen2.5:7b",
        "prompt": "hi",
        "stream": False
    }
)

print(
    response.json()["response"]
)

print(
    "TIME:",
    time.time() - start
)