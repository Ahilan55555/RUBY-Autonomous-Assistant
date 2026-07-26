from modules.perception.manager import (
    PerceptionManager
)

from modules.agents.reasoning_agent import (
    ReasoningAgent
)

manager = PerceptionManager()

reasoner = ReasoningAgent()

elements = manager.observe(
    "Firefox"
)

textbox = reasoner.find_best_textbox(
    elements
)

print(textbox)