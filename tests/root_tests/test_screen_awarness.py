import time

from modules.agents.screen_awareness_agent import (
    ScreenAwarenessAgent
)

agent = ScreenAwarenessAgent()

start = time.time()

result = agent.observe()

print(result)

print(
    "\nTIME:",
    time.time() - start
)