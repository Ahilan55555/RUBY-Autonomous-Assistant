import subprocess

def list_windows():

    result = subprocess.run(
        ["wmctrl", "-l"],
        capture_output=True,
        text=True
    )

    windows = []

    for line in result.stdout.splitlines():

        parts = line.split(None, 3)

        if len(parts) >= 4:

            windows.append(
                parts[3]
            )

    return {
        "success": True,
        "windows": windows
    }

def get_active_window():

    result = subprocess.run(
        [
            "xdotool",
            "getactivewindow",
            "getwindowname"
        ],
        capture_output=True,
        text=True
    )

    return {
        "success": True,
        "title": result.stdout.strip()
    }

def focus_window(title):

    subprocess.run(
        [
            "wmctrl",
            "-a",
            title
        ]
    )

    return {
        "success": True
    }

def close_window(title):

    subprocess.run(
        [
            "wmctrl",
            "-c",
            title
        ]
    )

    return {
        "success": True
    }

def _find_window_id(title):

    result = subprocess.run(
        ["wmctrl", "-l"],
        capture_output=True,
        text=True
    )

    for line in result.stdout.splitlines():

        if title.lower() in line.lower():

            return line.split()[0]

    return None


def minimize_window(title):

    window_id = _find_window_id(
        title
    )

    if not window_id:

        return {
            "success": False
        }

    subprocess.run(
        [
            "xdotool",
            "windowminimize",
            window_id
        ]
    )

    return {
        "success": True
    }

def maximize_window(title):

    window_id = _find_window_id(
        title
    )

    if not window_id:

        return {
            "success": False
        }

    subprocess.run(
        [
            "wmctrl",
            "-i",
            "-r",
            window_id,
            "-b",
            "add,maximized_vert,maximized_horz"
        ]
    )

    return {
        "success": True
    }

def get_window_rect(title):

    window_id = _find_window_id(
        title
    )

    if not window_id:

        return {
            "success": False
        }

    result = subprocess.run(
        [
            "xwininfo",
            "-id",
            window_id
        ],
        capture_output=True,
        text=True
    )

    output = result.stdout

    x = None
    y = None
    width = None
    height = None

    for line in output.splitlines():

        line = line.strip()

        if line.startswith(
            "Absolute upper-left X:"
        ):
            x = int(
                line.split(":")[1]
            )

        elif line.startswith(
            "Absolute upper-left Y:"
        ):
            y = int(
                line.split(":")[1]
            )

        elif line.startswith(
            "Width:"
        ):
            width = int(
                line.split(":")[1]
            )

        elif line.startswith(
            "Height:"
        ):
            height = int(
                line.split(":")[1]
            )

    return {
        "success": True,
        "x": x,
        "y": y,
        "width": width,
        "height": height
    }

def get_active_window_id():

    result = subprocess.run(
        [
            "xdotool",
            "getactivewindow"
        ],
        capture_output=True,
        text=True
    )

    window_id = result.stdout.strip()

    if not window_id:

        return {
            "success": False
        }

    return {
        "success": True,
        "window_id": window_id
    }

def get_window_rect_by_id(
    window_id
):

    result = subprocess.run(
        [
            "xdotool",
            "getwindowgeometry",
            str(window_id)
        ],
        capture_output=True,
        text=True
    )

    output = result.stdout

    try:

        x = y = width = height = 0

        for line in output.splitlines():

            if "Position:" in line:

                position = (
                    line.split(":")[1]
                    .strip()
                )

                coords = (
                    position.split(" ")[0]
                    .split(",")
                )

                x = int(coords[0])
                y = int(coords[1])

            elif "Geometry:" in line:

                geo = (
                    line.split(":")[1]
                    .strip()
                    .split("x")
                )

                width = int(geo[0])
                height = int(geo[1])

        return {
            "success": True,
            "x": x,
            "y": y,
            "width": width,
            "height": height
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }