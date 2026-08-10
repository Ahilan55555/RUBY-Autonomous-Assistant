from modules.automation.apps import (
    open_firefox
)

from core.world_state import (
    update_state,
    get_state
)

import pyautogui

import time


class BrowserNavigationAgent:


    def _prepare_browser(self):

        # Only open Firefox if it is not already the active application.
        # For now we use the world state that Ruby maintains.

        from core.world_state import get_state

        state = get_state()

        active_app = state.get(
            "active_app"
        )

        if active_app != "firefox":

            open_firefox()

            time.sleep(3)

        else:

            print(
                "[Browser Navigation] "
                "Firefox already active. Reusing it."
            )


    def open_google(self):

        self._prepare_browser()

        state = get_state()

        current_website = state.get(
            "current_website"
        )

        print(
            "[Browser Navigation] Current website:",
            current_website
        )

        if current_website == "google":

            print(
                "[Browser Navigation] Already on Google. Reusing it."
            )

            return

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

        time.sleep(2)

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

        time.sleep(2)

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

        time.sleep(2)

        update_state(
            "active_app",
            "firefox"
        )

        update_state(
            "current_website",
            "chatgpt"
        )