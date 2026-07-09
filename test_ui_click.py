from modules.agents.ui_agent import (
    UIAgent
)

ui = UIAgent()

textbox = ui.find_best(
    "Firefox",
    role="entry"
)

print(textbox)

result = ui.click_and_type(
    textbox,
    "Hello from Ruby"
)

print(result)