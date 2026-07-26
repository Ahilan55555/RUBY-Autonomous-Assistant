from core.mission import Mission
from core.mission_step import MissionStep


class MissionBuilder:

    def build(
        self,
        goal_context
    ):

        mission = Mission(
            goal=goal_context.command
        )

        command = goal_context.command.lower()

        steps = []

        if "search" in command:

            steps.append(

                MissionStep(

                    action="search",

                    target="robotics papers"

                )

            )

        if "read" in command:

            steps.append(

                MissionStep(

                    action="read",

                    target="first_result"

                )

            )

        if "summarize" in command:

            steps.append(

                MissionStep(

                    action="summarize",

                    target="current_document"

                )

            )

        if "save" in command:

            steps.append(

                MissionStep(

                    action="save",

                    target="summary.pdf"

                )

            )

        if "play" in command:

            steps.append(

                MissionStep(

                    action="play",

                    target="best_match"

                )

            )

        for step in steps:

            mission.add_step(
                step
            )

        return mission