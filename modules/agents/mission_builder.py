from core.mission import Mission


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

            steps.append({

                "action": "search",

                "target": "robotics papers"

            })

        if "read" in command:

            steps.append({

                "action": "read",

                "target": "first_result"

            })

        if "summarize" in command:

            steps.append({

                "action": "summarize",

                "target": "current_document"

            })

        if "save" in command:

            steps.append({

                "action": "save",

                "target": "summary.pdf"

            })

        if "play" in command:

            steps.append({

                "action": "play",

                "target": "best_match"

            })

        mission.steps = steps

        return mission