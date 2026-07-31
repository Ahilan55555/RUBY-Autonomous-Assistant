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