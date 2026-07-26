from modules.capabilities.browser.search import BrowserSearchCapability

capability = BrowserSearchCapability()

print(type(capability).__name__)

print(hasattr(capability, "prepare"))
print(hasattr(capability, "build_plan"))
print(hasattr(capability, "collect_result"))
print(hasattr(capability, "cleanup"))