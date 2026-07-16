from modules.capabilities.browser.search import (
    BrowserSearchCapability
)


class CapabilityRegistry:

    def __init__(self):

        self.capabilities = {

            "browser.search":

                BrowserSearchCapability()

        }

    def register(
        self,
        name,
        capability
    ):

        self.capabilities[name] = capability

    def get(
        self,
        name
    ):

        return self.capabilities.get(name)