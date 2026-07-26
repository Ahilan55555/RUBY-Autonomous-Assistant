from modules.agents.ui_agent import UIAgent

ui = UIAgent()

textbox = ui.find_textbox(
    "Firefox"
)

print(textbox)

print(
    ui.click(textbox)
)