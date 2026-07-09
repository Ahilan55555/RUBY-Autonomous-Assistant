from modules.perception.manager import PerceptionManager

from modules.perception.text_cleaner import (
    TextCleaner
)

class PageReader:

    def __init__(self):

        self.perception = PerceptionManager()

    def read(
        self,
        app
    ):

        elements = self.perception.observe_page(
            app
        )

        text = []

        for element in elements:

            name = element["name"].strip()

            if not name:
                continue

            role = element["role"]

            if role in (

                "heading",

                "paragraph",

                "text",

                "static",

                "document web"

            ):

                text.append(
                    name
                )

        cleaner = TextCleaner()

        text = cleaner.clean(
            text
        )


        return "\n".join(text)