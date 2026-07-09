from modules.agents.ui_agent import (
    UIAgent
)

ui = UIAgent()

textbox = ui.find_best(
    "Firefox",
    role="entry"
)

print(textbox)

button = ui.find_best(
    "Firefox",
    role="push button",
    text="Close"
)

print(button)

link = ui.find_best(
    "Firefox",
    role="link",
    text="GitHub"
)

print(link)