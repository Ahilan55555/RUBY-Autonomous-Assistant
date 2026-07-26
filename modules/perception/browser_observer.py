from modules.perception.manager import PerceptionManager

from modules.perception.observation_builder import ObservationBuilder


class BrowserObserver:

    def __init__(self):

        self.perception = PerceptionManager()

        self.builder = ObservationBuilder()

    def observe(self):

        elements = self.perception.observe_page(
            "firefox"
        )

        return self.builder.build(
            elements
        )