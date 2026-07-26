import time
from modules.agents.chat_agent import ChatAgent

agent = ChatAgent()

start = time.time()

response = agent.reply("hi")

print(response)

print(
    "\nTIME:",
    time.time() - start
)