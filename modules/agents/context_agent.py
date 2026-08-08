from modules.agents.situation_agent import (
    SituationAgent
)

from modules.agents.screen_awareness_agent import (
    ScreenAwarenessAgent
)


class ContextAgent:


    def build_context(self):

        situation = (

            SituationAgent()

            .analyze()
        )

        screen = (

            ScreenAwarenessAgent()

            .observe()
        )

        return {

            "success": True,

            "situation":
            situation,

            "screen":
            screen
        }


    def planner_context(
        self
    ):

        context = self.build_context()

        state = (
            context
            .get("situation", {})
            .get("state", {})
        )

        lines = []

        lines.append("Current Environment")
        lines.append("-------------------")

        lines.append(
            f"Active Application: {state.get('active_app', 'Unknown')}"
        )

        lines.append(
            f"Current Website: {state.get('current_website', 'Unknown')}"
        )

        lines.append(
            f"Working Directory: {state.get('working_directory', 'Unknown')}"
        )

        lines.append(
            f"Recent Task: {state.get('last_task', 'Unknown')}"
        )

        lines.append(
            f"Last Search: {state.get('last_search', 'None')}"
        )

        return "\n".join(lines)