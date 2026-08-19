from core.plan import Plan
from core.task import Task
from modules.capabilities.base import Capability
from modules.skills.open_url import open_url


class BrowserOpenURLCapability(Capability):

    def prepare(
        self,
        step,
        mission
    ):

        if mission is not None:

            mission.context.set(
                "url",
                step.query
            )

    def build_plan(
        self,
        step,
        mission
    ):

        url = step.query

        if not url:
            return None

        if not url.startswith(
            ("http://", "https://")
        ):

            url = "https://" + url

        task = Task(
            name="Open URL",
            capability="browser.open_url",
            parameters={
                "url": url
            }
        )

        plan = Plan(
            goal=f"Open {url}"
        )

        plan.add_task(
            task
        )

        return plan

    def execute(
        self,
        task,
        mission
    ):

        url = task.parameters.get(
            "url"
        )

        if not url:

            return {
                "success": False,
                "error": "No URL provided."
            }

        return open_url(
            url
        )

    def observe(self):

        return None

    def interpret(
        self,
        observation
    ):

        return observation

    def decide(
        self,
        interpretation,
        mission
    ):

        return interpretation

    def apply_result(
        self,
        mission,
        interpretation
    ):

        return interpretation

    def cleanup(
        self,
        mission
    ):

        pass