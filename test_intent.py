# test_intent.py

import core.register_capabilities

from core.intent_executor import (
    execute_intent
)

print(
    execute_intent(
        {
            "intent": "window",
            "target": "focus",
            "query": "Firefox"
        }
    )
)