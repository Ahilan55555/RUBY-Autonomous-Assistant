from modules.capabilities.registry import CapabilityRegistry

registry = CapabilityRegistry()

registry.register(
    "browser.search",
    "Search Capability"
)

print(
    registry.get(
        "browser.search"
    )
)