from modules.agents.ui_agent import (
    UIAgent
)

ui = UIAgent()

textbox = ui.find_textbox(
    "Firefox"
)

print(textbox)

buttons = ui.find_buttons(
    "Firefox"
)

print(len(buttons))

links = ui.find_links(
    "Firefox"
)

print(len(links))