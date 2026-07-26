# test_full_chatgpt_action.py

from modules.automation.screen_actions import (
    type_at_text
)

from modules.automation.keyboard_controller import (
    press_key
)

type_at_text(
    "Ask",
    "What is robotics?"
)

press_key(
    "enter"
)