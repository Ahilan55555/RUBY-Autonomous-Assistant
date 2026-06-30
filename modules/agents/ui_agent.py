from modules.automation.accessibility import (
    find_first_editable_entry,
    find_all_buttons,
    find_all_links,
    find_by_name
)
from modules.automation.mouse_controller import (
    move_mouse,
    left_click
)

from modules.automation.keyboard_controller import (
    type_text
)

from modules.perception.manager import (
    PerceptionManager
)

class UIAgent:

    def __init__(self):

        self.perception = (
            PerceptionManager()
        )

    def find_textbox(
        self,
        app
    ):

        return find_first_editable_entry(
            app
        )


    def find_buttons(
        self,
        app
    ):

        return find_all_buttons(
            app
        )


    def find_links(
        self,
        app
    ):

        return find_all_links(
            app
        )

    def click(
        self,
        element
    ):

        if element is None:

            return {
                "success": False,
                "error": "Element not found"
            }

        bounds = element.get("bounds")

        if bounds is None:

            return {
                "success": False,
                "error": "Element has no bounds"
            }

        x = (
            bounds["x"] +
            bounds["width"] // 2
        )

        y = (
            bounds["y"] +
            bounds["height"] // 2
        )

        move_mouse(
            x,
            y
        )

        left_click()

        return {
            "success": True
        }


    def find(
        self,
        app,
        role=None,
        text=None
    ):

        return self.perception.find(
            app,
            role,
            text
        )


    def click_and_type(
        self,
        element,
        text
    ):

        result = self.click(
            element
        )

        if not result["success"]:

            return result

        type_text(
            text
        )

        return {
            "success": True
        }