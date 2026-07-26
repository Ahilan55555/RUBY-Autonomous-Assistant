import core.register_capabilities

from modules.agents.desktop_agent import (
    DesktopAgent
)

from modules.agents.ui_learning_agent import (
    UILearningAgent
)

agent = DesktopAgent()

agent.lock_active_window()

visible = (
    agent.observe_locked_window_objects()
)

print(visible[:20])

learner = UILearningAgent()

result = learner.learn_text_object(
    "chatgpt",
    "textbox",
    visible,
    "Ask"
)

print(result)