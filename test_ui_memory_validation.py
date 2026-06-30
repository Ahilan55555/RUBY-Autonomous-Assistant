import core.register_capabilities

from modules.agents.desktop_agent import (
    DesktopAgent
)

from modules.agents.ui_memory_validator import (
    validate_ui_object
)

agent = DesktopAgent()

agent.lock_active_window()

visible = (
    agent.observe_locked_window_objects()
)

result = validate_ui_object(
    "chatgpt",
    "textbox",
    visible
)

print(result)