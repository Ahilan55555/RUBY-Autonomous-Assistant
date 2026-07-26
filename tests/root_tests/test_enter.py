# test_enter.py

from modules.automation.keyboard_controller import (
    press_key
)

input(
    "Focus ChatGPT textbox and press Enter..."
)

print(
    press_key("enter")
)