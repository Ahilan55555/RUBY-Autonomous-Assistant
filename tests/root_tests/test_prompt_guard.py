from modules.agents.llm_planner import LLMPlanner

planner = LLMPlanner()

tests = [
    "tell me a joke",
    "say something funny",
    "what is firefox",
    "how are you",
    "open firefox",
    "create file notes.txt"
    "shutdown the system",
    "click the close button",
    "close the current window",
    "open firefox and shutdown system"
]

for t in tests:

    print("\nINPUT:", t)

    plan = planner.plan(t)

    print(plan.tasks)