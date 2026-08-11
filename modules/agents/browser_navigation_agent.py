from modules.automation.apps import (
    open_firefox
)

from core.world_state import (
    update_state,

)

import subprocess

import pyautogui

import time


class BrowserNavigationAgent:


    def _prepare_browser(self):

        print(
            "[Browser Navigation] "
            "Opening/focusing Firefox."
        )

        open_firefox()

        time.sleep(1)

        result = subprocess.run(
            [
                "wmctrl",
                "-l",
                "-x"
            ],
            capture_output=True,
            text=True
        )

        print(
            "\n========== WINDOWS AFTER FOCUS =========="
        )

        print(
            result.stdout
        )

        print(
            "=========================================\n"
        )

        time.sleep(1)
        
    def open_google(self):

        self._prepare_browser()

        print(
            "[Browser Navigation] "
            "Navigating to Google."
        )

        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(0.5)

        pyautogui.write(
            "https://www.google.com",
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        time.sleep(3)

        update_state(
            "active_app",
            "firefox"
        )

        update_state(
            "current_website",
            "google"
        )

    def open_youtube(self):

        self._prepare_browser()

        print(
            "[Browser Navigation] "
            "Checking current Firefox page."
        )

        result = subprocess.run(
            [
                "wmctrl",
                "-l",
                "-x"
            ],
            capture_output=True,
            text=True
        )

        firefox_windows = [
            line
            for line in result.stdout.splitlines()
            if "Navigator.firefox_firefox" in line
        ]

        if firefox_windows:

            title = firefox_windows[0].lower()

            print(
                "[Browser Navigation] "
                "Firefox title:",
                title
            )

            if "youtube" in title:

                print(
                    "[Browser Navigation] "
                    "Already on YouTube."
                )

                update_state(
                    "active_app",
                    "firefox"
                )

                update_state(
                    "current_website",
                    "youtube"
                )

                return

        print(
            "[Browser Navigation] "
            "Navigating to YouTube."
        )

        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(0.5)

        pyautogui.write(
            "https://www.youtube.com",
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        time.sleep(3)

        update_state(
            "active_app",
            "firefox"
        )

        update_state(
            "current_website",
            "youtube"
        )

    def open_chatgpt(self):

        self._prepare_browser()

        print(
            "[Browser Navigation] "
            "Navigating to ChatGPT."
        )

        pyautogui.hotkey(
            "ctrl",
            "l"
        )

        time.sleep(0.5)

        pyautogui.write(
            "https://chatgpt.com",
            interval=0.02
        )

        pyautogui.press(
            "enter"
        )

        time.sleep(3)

        update_state(
            "active_app",
            "firefox"
        )

        update_state(
            "current_website",
            "chatgpt"
        )