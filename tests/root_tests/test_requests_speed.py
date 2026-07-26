import time
import requests

start = time.time()

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3.2:3b",
        "prompt": "hi",
        "stream": False
    }
)

print(response.json()["response"])

print(
    "\nTIME:",
    time.time() - start
)