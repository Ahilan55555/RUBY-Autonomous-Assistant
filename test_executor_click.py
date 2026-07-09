from core.executor import Executor

from core.action import Action

from modules.agents.ui_agent import UIAgent


ui = UIAgent()

textbox = ui.find_best(

    app="Firefox",

    role="text_input"

)

executor = Executor()

result = executor.execute(

    Action(

        action="click",

        target=textbox

    )

)

print(result)