from modules.automation.mouse_controller import (
    move_mouse,
    left_click,
    right_click,
    double_click
)

from modules.automation.keyboard_controller import (
    type_text
)

from modules.vision.screen_capture import (
    capture_screen
)

from modules.vision.ocr import (
    read_screen_boxes
)

import time

from modules.vision.window_capture import (
    capture_window_by_id
)

from modules.automation.window_controller import (
    get_active_window_id
)


def find_all_text(text, image_path):

    boxes = read_screen_boxes(
        image_path
    )

    text = text.lower()

    matches = []

    for box in boxes:

        if text in box["text"].lower():

            matches.append(
                {
                    "text": box["text"],
                    "x": box["x"] + box["w"] // 2,
                    "y": box["y"] + box["h"] // 2
                }
            )

    return matches


def find_text(text, image_path):

    matches = find_all_text(
        text,
        image_path
    )

    if not matches:

        return {
            "success": False
        }
    print(matches)
    best = max(
        matches,
        key=lambda m: m["y"]
    )

    return {
        "success": True,
        **best
    }



def click_text(
    text,
    window_id=None
):

    print("CLICK START")

    shot = screenshot(
        window_id
    )

    if shot is None:
        return {
            "success": False
        }

    image_path = shot["path"]

    result = find_text(
        text,
        image_path
    )

    print("OCR DONE")

    if not result["success"]:
        return result

    print("MOVE")

    screen_x = result["x"]
    screen_y = result["y"]

    if window_id is not None:

        screen_x += shot["x"]
        screen_y += shot["y"]

    move_mouse(
        screen_x,
        screen_y
    )

    print("CLICK")

    left_click()

    print("CLICK FINISHED")

    return {
        "success": True,
        "x": result["x"],
        "y": result["y"]
    }

def screenshot(window_id=None):

    if window_id is None:

        result = capture_screen(
            "temp/screenshot.png"
        )

    else:

        result = capture_window_by_id(
            window_id,
            "temp/window_screenshot.png"
        )

    if not result["success"]:
        return None

    return result

def double_click_text(text):

    image_path = screenshot()

    result = find_text(
        text,
        image_path
    )

    if not result["success"]:
        return result

    move_mouse(
        result["x"],
        result["y"]
    )

    double_click()

    return {
        "success": True
    }

def right_click_text(text):

    image_path = screenshot()

    result = find_text(
        text,
        image_path
    )

    if not result["success"]:
        return result

    move_mouse(
        result["x"],
        result["y"]
    )

    right_click()

    return {
        "success": True
    }


def type_at_text(
    text_to_find,
    text_to_type,
    window_id=None
):

    print("A", get_active_window_id())

    result = click_text(
        text_to_find,
        window_id
    )

    print("B", get_active_window_id())

    if not result["success"]:
        return result

    time.sleep(0.4)

    print("C", get_active_window_id())

    type_text(
        text_to_type
    )

    print("D", get_active_window_id())

    return {
        "success": True
    }