from modules.vision.window_capture import (
    capture_window,
    capture_active_window,
    capture_window_by_id
)

from modules.vision.ocr import (
    get_visible_texts,
    read_screen_text,
    read_screen_boxes
)



def observe_window(title):

    result = capture_window(
        title,
        "temp/window_observe.png"
    )

    if not result["success"]:
        return ""

    return read_screen_text(
        result["path"]
    )


def observe_active_window():

    result = capture_active_window()

    if not result["success"]:
        return ""

    return read_screen_text(
        result["path"]
    )


def observe_window_boxes(title):

    result = capture_window(
        title,
        "temp/window_boxes.png"
    )

    if not result["success"]:
        return []

    return get_visible_texts(
        result["path"]
    )

def observe_window_boxes_by_id(
    window_id
):

    result = capture_window_by_id(
        window_id,
        "temp/window_objects.png"
    )

    if not result["success"]:

        return []

    return read_screen_boxes(
        result["path"]
    )