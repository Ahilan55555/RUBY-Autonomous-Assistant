import time

from modules.agents.desktop_assistant_agent import (
    DesktopAssistantAgent
)

agent = DesktopAssistantAgent()

start = time.time()

print(
    agent.what_am_i_doing()
)

print(
    "\nFIRST:",
    time.time() - start
)

start = time.time()

print(
    agent.what_am_i_doing()
)

print(
    "\nSECOND:",
    time.time() - start
)