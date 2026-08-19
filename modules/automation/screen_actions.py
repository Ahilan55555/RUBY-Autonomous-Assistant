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
    get_active_window_id,
    get_application_window_id
)


def normalize_ocr_text(text):

    return (
        text
        .strip()
        .strip('"')
        .strip("'")
        .strip()
        .lower()
    )


def find_all_text(text, image_path):

    boxes = read_screen_boxes(
        image_path
    )

    print("\n========== OCR BOXES ==========")

    for box in boxes:
        print(
            repr(box["text"]),
            "x=", box["x"],
            "y=", box["y"],
            "w=", box["w"],
            "h=", box["h"]
        )

    print("================================\n")

    target = normalize_ocr_text(
        text
    )

    matches = []

    for box in boxes:

        candidate = normalize_ocr_text(
            box["text"]
        )

        if candidate == target:

            matches.append(
                {
                    "text": box["text"],
                    "x": box["x"] + box["w"] // 2,
                    "y": box["y"] + box["h"] // 2
                }
            )

    return matches

def find_accessibility_text(
    text,
    app="Firefox"
):

    from modules.perception.manager import (
        PerceptionManager
    )

    perception = PerceptionManager()

    elements = perception.observe(
        app
    )

    target = text.lower().strip()

    exact_matches = []
    partial_matches = []

    for element in elements:

        name = element.get(
            "name",
            ""
        )

        if not name:
            continue

        name_normalized = name.lower().strip()

        bounds = element.get(
            "bounds"
        )

        if not bounds:
            continue

        if bounds["width"] <= 0:
            continue

        if bounds["height"] <= 0:
            continue

        if bounds["x"] < 0:
            continue

        if bounds["y"] < 0:
            continue

        # -----------------------------------------
        # State filtering
        # -----------------------------------------

        states = element.get(
            "states"
        ) or []

        state_text = " ".join(
            str(state).lower()
            for state in states
        )

        # A screen click should only target an
        # element that is actually showing.
        if "showing" not in state_text:
            continue

        if "visible" not in state_text:
            continue

        if "enabled" not in state_text:
            continue

        # -----------------------------------------
        # Candidate
        # -----------------------------------------

        candidate = {
            "text": name,
            "x": (
                bounds["x"]
                + bounds["width"] // 2
            ),
            "y": (
                bounds["y"]
                + bounds["height"] // 2
            ),
            "source": "accessibility",
            "role": element.get(
                "role"
            ),
            "bounds": bounds,
            "states": states
        }

        # -----------------------------------------
        # Prefer exact text matches
        # -----------------------------------------

        if name_normalized == target:

            exact_matches.append(
                candidate
            )

        elif target in name_normalized:

            partial_matches.append(
                candidate
            )

    # ---------------------------------------------
    # Prefer exact visible/showing match
    # ---------------------------------------------

    matches = (
        exact_matches
        if exact_matches
        else partial_matches
    )

    if not matches:

        return {
            "success": False
        }

    # ---------------------------------------------
    # Prefer interactive roles
    # ---------------------------------------------

    role_priority = {
        "push button": 100,
        "link": 90,
        "menu item": 80,
        "list item": 70,
        "button": 70
    }

    matches.sort(
        key=lambda item:
            role_priority.get(
                item.get("role"),
                0
            ),
        reverse=True
    )

    selected = matches[0]

    print(
        f"[Accessibility] "
        f"Found {len(matches)} matching candidates."
    )

    for index, candidate in enumerate(matches):

        print(
            f"[Accessibility] "
            f"Candidate {index}: "
            f"{candidate['text']} | "
            f"role={candidate['role']} | "
            f"position="
            f"{candidate['x']},"
            f"{candidate['y']}"
        )

    print(
        "[Accessibility] "
        f"Selected: {selected['text']}"
    )

    return {
        "success": True,
        **selected
    }

def find_text(
    text,
    image_path
):

    accessibility_result = (
        find_accessibility_text(
            text
        )
    )

    if accessibility_result["success"]:

        print(
            "[Screen Actions] "
            "Found through accessibility."
        )

        return accessibility_result

    print(
        "[Screen Actions] "
        "Accessibility failed. "
        "Using OCR fallback."
    )

    matches = find_all_text(
        text,
        image_path
    )

    if not matches:

        return {
            "success": False
        }

    print(matches)

    best = matches[0]

    return {
        "success": True,
        **best,
        "source": "ocr"
    }


def click_text(
    text,
    window_id=None,
    app="firefox",
    delay=0.5
):

    print("CLICK START")

    # -----------------------------------------
    # Resolve application window
    # -----------------------------------------

    if window_id is None:

        window = get_application_window_id(
            app
        )

        if not window["success"]:

            return window

        window_id = window["window_id"]

    print(
        "[Screen Actions] "
        f"Using window: {window_id}"
    )
    # -----------------------------------------
    # Try accessibility first
    # -----------------------------------------

    accessibility_result = find_accessibility_text(
        text,
        app="Firefox"
    )

    if accessibility_result.get("success"):

        print(
            "[Screen Actions] "
            "Using accessibility result."
        )

        x = accessibility_result["x"]
        y = accessibility_result["y"]

        move_mouse(
            x,
            y
        )

        time.sleep(delay)

        left_click()

        return {
            "success": True,
            "method": "accessibility",
            "text": text,
            "x": x,
            "y": y
        }

    # -----------------------------------------
    # Capture window
    # -----------------------------------------

    shot = screenshot(
        window_id
    )

    if shot is None:

        print(
            "[Screen Actions] "
            f"Window {window_id} could not be captured."
        )

        # Try to reacquire the application window

        window = get_application_window_id(
            app
        )

        if not window["success"]:

            return {
                "success": False,
                "error": (
                    f"Could not reacquire {app} window"
                )
            }

        window_id = window["window_id"]

        print(
            "[Screen Actions] "
            f"Reacquired window: {window_id}"
        )

        shot = screenshot(
            window_id
        )

        if shot is None:

            return {
                "success": False,
                "error": (
                    "Could not capture "
                    "reacquired window"
                )
            }

    # -----------------------------------------
    # Find target
    # -----------------------------------------

    image_path = shot["path"]

    result = find_text(
        text,
        image_path
    )

    print("OCR DONE")

    if not result["success"]:

        return {
            "success": False,
            "error": (
                f"Could not find '{text}'"
            )
        }

    # -----------------------------------------
    # Calculate click position
    # -----------------------------------------

    screen_x = result["x"]
    screen_y = result["y"]

    # Accessibility coordinates are already
    # global screen coordinates.
    #
    # OCR coordinates are relative to the
    # captured window.

    if (
        result.get("source") != "accessibility"
    ):

        screen_x += shot["x"]
        screen_y += shot["y"]

    print(
        "[Screen Actions] "
        f"Target: {result['text']}"
    )

    print(
        "[Screen Actions] "
        f"Click position: {screen_x}, {screen_y}"
    )

    # -----------------------------------------
    # Perform ONE click
    # -----------------------------------------

    print("MOVE")

    move_mouse(
        screen_x,
        screen_y
    )

    time.sleep(0.1)

    print("CLICK")

    left_click()

    print("CLICK FINISHED")

    time.sleep(delay)

    # -----------------------------------------
    # Action completed
    #
    # Verification should happen outside
    # this low-level click function.
    # -----------------------------------------

    return {
        "success": True,
        "x": screen_x,
        "y": screen_y,
        "source": result.get("source"),
        "verified": False
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