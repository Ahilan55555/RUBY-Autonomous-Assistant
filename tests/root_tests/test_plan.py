from core.plan import Plan
from core.task import Task

plan = Plan(
    goal="Search Google"
)

plan.add_task(
    Task("Open Browser")
)

plan.add_task(
    Task("Search")
)

print(plan.goal)
print(plan.tasks)