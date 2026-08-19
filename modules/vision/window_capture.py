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

    print(
        "[Window Capture] Window ID:",
        window_id
    )

    print(
        "[Window Capture] Rect:",
        rect
    )

    image = Image.open(
        "temp/fullscreen.png"
    )

    screen_width, screen_height = image.size

    x = rect["x"]
    y = rect["y"]
    width = rect["width"]
    height = rect["height"]

    print(
        "[Window Capture] Screen:",
        screen_width,
        "x",
        screen_height
    )

    print(
        "[Window Capture] Requested:",
        x,
        y,
        width,
        height
    )

    if width <= 0 or height <= 0:

        return {
            "success": False,
            "error": (
                "Invalid window dimensions: "
                f"{width}x{height}"
            )
        }

    left = max(
        0,
        x
    )

    top = max(
        0,
        y
    )

    right = min(
        screen_width,
        x + width
    )

    bottom = min(
        screen_height,
        y + height
    )

    if right <= left or bottom <= top:

        return {
            "success": False,
            "error": (
                "Window rectangle is outside "
                "the captured screen."
            )
        }

    cropped = image.crop(
        (
            left,
            top,
            right,
            bottom
        )
    )

    if cropped.width <= 0 or cropped.height <= 0:

        return {
            "success": False,
            "error": "Window crop is empty."
        }

    cropped.save(
        output
    )

    return {
        "success": True,
        "path": output,
        "x": left,
        "y": top,
        "width": cropped.width,
        "height": cropped.height
    }