# test_capability_bug.py

import core.register_capabilities

from core.capability_registry import (
    show_capabilities,
    has_capability
)

print(show_capabilities())

print(
    has_capability(
        "screen",
        "click_text"
    )
)