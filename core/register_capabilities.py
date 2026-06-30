from core.capability_registry import (
    register_capability
)
from core.capability_registry import (
    capabilities
)

print(
    "REGISTER ID:",
    id(capabilities)
)
# Apps
register_capability(
    "open_app",
    "firefox"
)

register_capability(
    "open_app",
    "sublime"
)

# Websites
register_capability(
    "open_website",
    "github"
)

register_capability(
    "open_website",
    "youtube"
)

# Terminal
register_capability(
    "terminal",
    "pwd"
)

# Files
register_capability(
    "file",
    "list"
)

register_capability(
    "file",
    "create_folder"
)

register_capability(
    "file",
    "create_file"
)

register_capability(
    "file",
    "delete_folder"
)

register_capability(
    "file",
    "read"
)

register_capability(
    "file",
    "write"
)

# Project
register_capability(
    "project",
    "analyze"
)

# Search
register_capability(
    "google_search"
)

# Python
register_capability(
    "python"
)

# Mouse

register_capability("mouse", "move")
register_capability("mouse", "click")
register_capability("mouse", "double_click")
register_capability("mouse", "right_click")

# Keyboard

register_capability("keyboard", "type")
register_capability("keyboard", "enter")
register_capability("keyboard", "hotkey")

# Windows

register_capability("window", "focus")
register_capability("window", "close")
register_capability("window", "minimize")
register_capability("window", "maximize")
register_capability("window", "list")
register_capability("window", "active")

register_capability(
    "screen",
    "click_text"
)

register_capability(
    "screen",
    "double_click_text"
)

register_capability(
    "screen",
    "right_click_text"
)

register_capability(
    "screen",
    "type_at_text"
)
register_capability(
    "browser",
    "search_google"
)

register_capability(
    "browser",
    "search_youtube"
)

register_capability(
    "browser",
    "ask_chatgpt"
)
