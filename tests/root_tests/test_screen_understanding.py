from modules.agents.screen_awareness_agent import (
    ScreenAwarenessAgent
)

from modules.agents.screen_understanding_agent import (
    ScreenUnderstandingAgent
)

screen = ScreenAwarenessAgent()

understanding = ScreenUnderstandingAgent()

result = screen.observe()

print(
    understanding.understand(
        result["raw_text"]
    )
)