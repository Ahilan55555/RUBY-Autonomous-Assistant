from PIL import Image

from modules.vision.screen_capture import (
    capture_screen
)

from modules.automation.window_controller import (
    get_window_rect,
    get_active_window_id,
    get_window_rect_by_id
)

from modules.automation.window_controller import (
    get_active_window_id,
    get_window_rect_by_id
)

def capture_window(
    title,
    output="temp/window_capture.png"
):

    screen = capture_screen(
        "temp/fullscreen.png"
    )

    if not screen["success"]:

        return screen

    rect = get_window_rect(
        title
    )

    if not rect["success"]:

        return rect

    image = Image.open(
        "temp/fullscreen.png"
    )

    cropped = image.crop(
        (
            rect["x"],
            rect["y"],
            rect["x"] + rect["width"],
            rect["y"] + rect["height"]
        )
    )

    cropped.save(
        output
    )

    return {
        "success": True,
        "path": output
    }


def capture_active_window(
    output="temp/active_window.png"
):

    screen = capture_screen(
        "temp/fullscreen.png"
    )

    if not screen["success"]:

        return screen

    active = get_active_window_id()

    if not active["success"]:

        return active

    rect = get_window_rect_by_id(
        active["window_id"]
    )

    if not rect["success"]:

        return rect

    image = Image.open(
        "temp/fullscreen.png"
    )

    cropped = image.crop(
        (
            rect["x"],
            rect["y"],
            rect["x"] + rect["width"],
            rect["y"] + rect["height"]
        )
    )

    cropped.save(
        output
    )

    return {
        "success": True,
        "path": output
    }


def capture_window_by_id(
    window_id,
    output="temp/window_by_id.png"
):

    screen = capture_screen(
        "temp/fullscreen.png"
    )

    if not screen["success"]:
        return screen

    rect = get_window_rect_by_id(
        window_id
    )

    if not rect["success"]:
        return rect

    image = Image.open(
        "temp/fullscreen.png"
    )

    cropped = image.crop(
        (
            rect["x"],
            rect["y"],
            rect["x"] + rect["width"],
            rect["y"] + rect["height"]
        )
    )

    cropped.save(
        output
    )

    return {
        "success": True,
        "path": output,
        "x": rect["x"],
        "y": rect["y"],
        "width": rect["width"],
        "height": rect["height"]
    }