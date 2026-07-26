import core.register_capabilities

from core.intent_executor import (
    execute_intent
)


tasks = [

    {
        "intent": "window",
        "target": "focus",
        "query": "Firefox"
    },

    {
        "intent": "screen",
        "target": "type_at_text",
        "query": "Ask|What is robotics?"
    },

    {
        "intent": "keyboard",
        "target": "enter"
    }
]

for task in tasks:

    result = execute_intent(task)

    print(result)