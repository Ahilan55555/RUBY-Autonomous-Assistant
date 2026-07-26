import time

from modules.agents.chat_agent import ChatAgent

start = time.time()

response = ChatAgent().reply(
    "what is robotics"
)

print(response)

print(
    "\nTIME:",
    time.time() - start
)