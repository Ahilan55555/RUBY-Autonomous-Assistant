from modules.agents.llm_planner import LLMPlanner

planner = LLMPlanner()

tests = [

    "shutdown system",

    "click the close button",

    "close current window",

    "open firefox",

    "create file notes.txt"
]

for t in tests:

    print("\nINPUT:", t)

    plan = planner.plan(t)

    print("GOAL:", plan.goal)

    print("TASKS:", plan.tasks)