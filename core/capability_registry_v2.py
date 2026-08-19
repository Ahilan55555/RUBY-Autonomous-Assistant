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
def capability_exists(
    intent
):

    return intent in capabilities

# -------------------------------------------------
# Register Capability
# -------------------------------------------------

def register_capability(
    intent,
    capability,
    target=None,
    purpose="",
    limitations="",
    examples=None
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

    capabilities[intent][target] = {
        "object": capability,
        "purpose": purpose,
        "limitations": limitations,
        "examples": examples or []
    }


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

    data = capabilities[intent].get(target)

    if data is None:
        return None

    return data["object"]


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

    lines = []

    for intent, targets in capabilities.items():

        lines.append("=" * 40)

        lines.append(f"Intent: {intent}")
        lines.append("")

        for target, data in targets.items():

            lines.append(f"Target: {target}")
            lines.append("")

            lines.append(
                f"Purpose: {data['purpose'] or 'Not specified'}"
            )

            lines.append("")

            lines.append(
                f"Limitations: {data['limitations'] or 'None'}"
            )

            lines.append("")

            lines.append("Examples:")

            if data["examples"]:

                for example in data["examples"]:

                    lines.append(
                        f"  - {example}"
                    )

            else:

                lines.append("  - None")

            lines.append("")

    lines.append("=" * 40)

    return "\n".join(lines)

def planner_capabilities():

    result = []

    for intent, targets in capabilities.items():

        for target, data in targets.items():

            # Do not expose legacy/global capabilities
            # with no explicit target to the LLM planner.
            if target is None:
                continue

            result.append({

                "intent": intent,

                "target": target,

                "purpose": data["purpose"],

                "limitations": data["limitations"],

                "examples": data["examples"]

            })

    return result