from modules.agents.ui_agent import UIAgent

ui = UIAgent()

github = ui.find(
    "Firefox",
    text="GitHub"
)

print(github)