from core.observation import Observation

from modules.perception.browser_observer import BrowserObserver


class TaskObserver:

    def __init__(self):

        self.browser = BrowserObserver()

    def observe(
        self,
        task
    ):

        task_name = getattr(task, "name", "").lower()

        if "browser" in task_name:

            return self.browser.observe()

        return Observation()