import core.register_capabilities

from core.intent_executor import (
    execute_intent
)

print(
    execute_intent(
        {
            "intent": "screen",
            "target": "click_text",
            "query": "Ask"
        }
    )
)