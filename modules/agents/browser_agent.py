from modules.automation.browser import (
    open_google,
    open_youtube,
    open_chatgpt
)

from modules.automation.screen_actions import (
    type_at_text
)

from modules.automation.keyboard_controller import (
    press_key
)

from modules.automation.window_session import (
    focus_and_lock
)

import time

from modules.automation.window_controller import (
    get_active_window_id
)

class BrowserAgent:

    def search_google(
        self,
        query
    ):

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        open_google()

        time.sleep(3)

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        window_id = lock["window_id"]

        result = type_at_text(
            "Search",
            query,
            window_id
        )

        if not result["success"]:
            return result

        time.sleep(0.5)

        press_key(
            "enter"
        )

        return {
            "success": True,
            "query": query
        }


    def search_google(
        self,
        query
    ):

        print("\nSTEP 1: Focus Firefox")

        lock = focus_and_lock(
            "Firefox"
        )

        print(lock)

        if not lock["success"]:
            return lock

        print(
            "ACTIVE:",
            get_active_window_id()
        )

        print("\nSTEP 2: Open Google")

        open_google()

        time.sleep(3)

        print(
            "ACTIVE:",
            get_active_window_id()
        )

        print("\nSTEP 3: Lock Again")

        lock = focus_and_lock(
            "Firefox"
        )

        print(lock)

        print(
            "ACTIVE:",
            get_active_window_id()
        )

        if not lock["success"]:
            return lock

        window_id = lock["window_id"]

        print("\nSTEP 4: Click Search")

        result = type_at_text(
            "Search",
            query,
            window_id
        )

        print(result)

        print(
            "ACTIVE:",
            get_active_window_id()
        )

        if not result["success"]:
            return result

        print("\nSTEP 5: Wait")

        time.sleep(2)

        print(
            "ACTIVE:",
            get_active_window_id()
        )

        print("\nSTEP 6: Press Enter")

        press_key("enter")

        print(
            "ACTIVE:",
            get_active_window_id()
        )

        return {
            "success": True
        }


    def ask_chatgpt(
        self,
        prompt
    ):

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        open_chatgpt()

        time.sleep(5)

        lock = focus_and_lock(
            "Firefox"
        )

        if not lock["success"]:
            return lock

        window_id = lock["window_id"]

        result = type_at_text(
            "Ask anything",
            prompt,
            window_id
        )

        if not result["success"]:
            return result

        time.sleep(0.5)

        press_key(
            "enter"
        )

        return {
            "success": True,
            "prompt": prompt
        }