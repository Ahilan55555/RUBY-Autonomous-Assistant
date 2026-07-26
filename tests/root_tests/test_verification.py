from modules.agents.verification_agent import (
    VerificationAgent
)

agent = VerificationAgent()

screen = """
ChatGPT
Ask anything
"""

print(
    agent.text_exists(
        "Ask",
        screen
    )
)