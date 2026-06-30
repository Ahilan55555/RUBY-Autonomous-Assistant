from modules.memory.ui_memory import (
    remember_ui_object
)


class UILearningAgent:

    def learn_text_object(
        self,
        app,
        name,
        visible_objects,
        target_text
    ):

        target_text = (
            target_text.lower()
        )

        for obj in visible_objects:

            if (
                target_text
                in
                obj["text"].lower()
            ):

                remember_ui_object(
                    app,
                    name,
                    obj
                )

                return obj

        return None