from modules.memory.long_term_memory import load_memory

from core.intent_resolver import resolve_intent


load_memory()


task = {

    "intent": "open_app",

    "target": "browser"
}


print(

    resolve_intent(task)
)