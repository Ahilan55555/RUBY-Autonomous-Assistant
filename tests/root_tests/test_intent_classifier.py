from modules.agents.intent_classifier import (
    IntentClassifier
)

c = IntentClassifier()

tests = [

    "hi",

    "open firefox",

    "what is firefox",

    "open firefox and tell me what firefox is",

    "could you open github",

    "please create a file called test.txt"
]

for t in tests:

    print(
        t,
        "->",
        c.classify(t)
    )