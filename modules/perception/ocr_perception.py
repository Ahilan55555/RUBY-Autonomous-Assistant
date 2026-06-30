from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.ocr import (
    read_screen_boxes
)

from modules.perception.ui_element import (
    create_ui_element
)


def observe():

    result = capture_screen(
        "temp/perception.png"
    )

    if not result["success"]:
        return []

    boxes = read_screen_boxes(
        result["path"]
    )

    elements = []

    for box in boxes:

        elements.append(

            create_ui_element(

                source="ocr",

                name=box["text"],

                role="text",

                bounds={
                    "x": box["x"],
                    "y": box["y"],
                    "width": box["w"],
                    "height": box["h"]
                }

            )

        )

    return elements