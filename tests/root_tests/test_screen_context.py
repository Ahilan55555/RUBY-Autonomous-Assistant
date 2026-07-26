from modules.agents.screen_understanding_agent import (
    ScreenUnderstandingAgent
)

agent = (
    ScreenUnderstandingAgent()
)

agent.memory.add(
    "Editing OCR code"
)

agent.memory.add(
    "Running OCR tests"
)

agent.memory.add(
    "Checking OCR results"
)

print(
    agent.get_recent_context()
)