from modules.agents.adaptive_planner import (
    AdaptivePlanner
)

planner = AdaptivePlanner()

tests = [

    "hi",

    "open firefox",

    "can you open firefox",

    "what is firefox",

    "open firefox and explain firefox",

    "create file notes.txt",

    "open github and tell me about github"
]

for text in tests:

    plan = planner.recover(text)

    print("\nINPUT:", text)

    print("TASKS:", plan.tasks)