"""
Capability Registry V2

Purpose:
    Stores and returns capability OBJECTS instead of only checking
    whether a capability exists.

Architecture:

    register_capability()
            │
            ▼
      capabilities
            │
            ▼
     get_capability()
            │
            ▼
   Capability Object

Example:

    register_capability(
        "google_search",
        BrowserSearchCapability()
    )

    capability = get_capability(
        "google_search"
    )

    capability.execute(...)
"""

# -------------------------------------------------
# Capability Storage
# -------------------------------------------------

capabilities = {}


# -------------------------------------------------
# Register Capability
# -------------------------------------------------

def register_capability(
    intent,
    capability,
    target=None
):
    """
    Registers a capability object.

    Examples:

        register_capability(
            "google_search",
            BrowserSearchCapability()
        )

        register_capability(
            "file",
            FileReadCapability(),
            "read"
        )
    """

    if intent not in capabilities:
        capabilities[intent] = {}

    capabilities[intent][target] = capability


# -------------------------------------------------
# Get Capability
# -------------------------------------------------

def get_capability(
    intent,
    target=None
):
    """
    Returns the capability object.

    Returns:
        Capability object if found.
        None otherwise.
    """

    if intent not in capabilities:
        return None

    return capabilities[intent].get(target)


# -------------------------------------------------
# Has Capability
# -------------------------------------------------

def has_capability(
    intent,
    target=None
):
    """
    Returns True if a capability exists.
    """

    return (
        get_capability(
            intent,
            target
        )
        is not None
    )


# -------------------------------------------------
# Show Registry
# -------------------------------------------------

def show_capabilities():
    """
    Returns the entire capability registry.
    """

    return capabilities


def capability_summary():

    descriptions = {

        "open_app":
            "Launch an installed desktop application.",

        "open_website":
            "Open a supported website in the browser.",

        "google_search":
            "Search Google for the provided query.",

        "browser":
            (
                "Perform browser-specific actions such as "
                "searching YouTube, searching Google, or "
                "interacting with ChatGPT."
            ),

        "terminal":
            "Execute supported terminal commands.",

        "file":
            "Read, write, create, delete and list files.",

        "project":
            "Analyze or inspect the current project.",

        "python":
            "Execute Python scripts.",

        "keyboard":
            "Perform keyboard input such as typing or pressing keys.",

        "mouse":
            "Perform mouse actions such as click or move.",

        "screen":
            "Interact with visible screen text using OCR.",

        "window":
            "Control application windows."
    }

    limitations = {

        "open_website":
            "Only supports registered websites.",

        "google_search":
            "Searches Google only. It does not search YouTube unless requested.",

        "browser":
            "Use only for browser-specific actions.",

        "terminal":
            "Only supported terminal commands may be executed.",

        "file":
            "Only supported file operations may be executed."
    }

    lines = []

    for intent, targets in capabilities.items():

        lines.append("=" * 40)

        lines.append(
            f"Intent: {intent}"
        )

        if len(targets) == 1 and None in targets:

            lines.append(
                "Targets: None"
            )

        else:

            lines.append(
                "Targets:"
            )

            for target in targets:

                if target is None:
                    continue

                lines.append(
                    f"  - {target}"
                )

        if intent in descriptions:

            lines.append("")
            lines.append(
                f"Purpose: {descriptions[intent]}"
            )

        if intent in limitations:

            lines.append(
                f"Limitations: {limitations[intent]}"
            )

        lines.append("")

    return "\n".join(lines)