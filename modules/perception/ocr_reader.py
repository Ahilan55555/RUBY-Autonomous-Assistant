from modules.perception.ocr_perception import (
    observe
)


class OCRReader:

    def read(
        self
    ):

        elements = observe()

        text = []

        for element in elements:

            name = element["name"]

            if not name:
                continue

            name = name.strip()

            if not name:
                continue

            text.append(name)

        return text