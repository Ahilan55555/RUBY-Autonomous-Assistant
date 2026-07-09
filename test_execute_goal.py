from modules.agents.browser_agent import BrowserAgent
from modules.agents.planner import Planner

planner = Planner()

browser = BrowserAgent()

goal = planner.interpret(

    "search google robotics"

)

print(goal)

result = browser.execute_goal(
    goal
)

print(result)