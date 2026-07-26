from modules.agents.planner import Planner

planner = Planner()

goal = planner.interpret(

    "search google robotics"

)

print(goal)