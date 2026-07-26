from modules.agents.llm_planner import (
    LLMPlanner
)

planner = LLMPlanner()

tests = [

    "open github and tell me about github",

    "open firefox and explain firefox",

    "open github and open firefox",

    "create file notes.txt and explain firefox"
]

for text in tests:

    print("\nINPUT:", text)

    plan = planner.plan(text)

    print(plan.tasks)