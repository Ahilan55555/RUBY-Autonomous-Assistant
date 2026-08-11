import subprocess

import time


def open_firefox():

    print(
        "[Firefox] Checking for existing Firefox window..."
    )

    try:

        result = subprocess.run(
            [
                "wmctrl",
                "-l",
                "-x"
            ],
            capture_output=True,
            text=True
        )

        windows = result.stdout.splitlines()

        firefox_windows = [

            line

            for line in windows

            if ".Firefox" in line
            or "firefox.Firefox" in line
            or "Firefox" in line

        ]

        if firefox_windows:

            print(
                "[Firefox] Existing Firefox window found."
            )

            # Use the first detected Firefox window.
            # We will explicitly activate it.
            window_id = firefox_windows[0].split()[0]

            print(
                "[Firefox] Activating window:",
                window_id
            )

            subprocess.run(
                [
                    "wmctrl",
                    "-ia",
                    window_id
                ],
                check=False,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            time.sleep(1)

            return True

    except Exception as e:

        print(
            "[Firefox] Window detection failed:",
            e
        )

    print(
        "[Firefox] No Firefox window found. Starting Firefox."
    )

    subprocess.Popen(
        ["firefox"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(4)

    return True

def open_sublime():

    subprocess.Popen(
        ["subl"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    time.sleep(2)

    try:

        subprocess.run(
            [
                "wmctrl",
                "-a",
                "Sublime"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

    except Exception:

        pass