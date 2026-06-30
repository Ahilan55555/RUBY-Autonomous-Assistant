from modules.agents.ui_agent import UIAgent

ui = UIAgent()

textbox = ui.find_textbox(
    "Firefox"
)

print(
    ui.click_and_type(
        textbox,
        "Hello Ruby"
    )
)