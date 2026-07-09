from modules.agents.ui_agent import UIAgent
from modules.agents.goal_executor import GoalExecutor

from core.task_builder import TaskBuilder
from core.plan import Plan


ui = UIAgent()

textbox = ui.find_best(
    app="Firefox",
    role="text_input"
)

builder = TaskBuilder()

task = builder.text_input(
    textbox,
    "Hello Ruby"
)

plan = Plan(
    goal="Test"
)

plan.add_task(task)

executor = GoalExecutor()

print(
    executor.run(plan)
)