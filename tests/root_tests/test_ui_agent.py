from modules.agents.ui_agent import UIAgent

ui = UIAgent()

textbox = ui.find_textbox("Firefox")
print("TEXTBOX")
print(textbox)

print()

buttons = ui.find_buttons("Firefox")
print("BUTTONS")
for button in buttons[:10]:
    print(button["name"], button["bounds"])

print()

links = ui.find_links("Firefox")
print("LINKS")
for link in links[:10]:
    print(link["name"])