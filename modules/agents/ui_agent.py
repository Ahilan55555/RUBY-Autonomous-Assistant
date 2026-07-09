
from modules.automation.mouse_controller import (
    move_mouse,
    left_click,
    right_click,
    double_click
    
)

from modules.automation.keyboard_controller import (
    type_text,
    press_key
)

import time


from modules.perception.manager import (
    PerceptionManager
)

from modules.agents.reasoning_agent import (
    ReasoningAgent
)

class UIAgent:

    def __init__(self):

        self.perception = PerceptionManager()

        self.reasoner = ReasoningAgent()

    def find_textbox(
        self,
        app
    ):

        elements = self.perception.observe(
            app
        )

        return self.reasoner.find_best_textbox(
            elements
        )


    def find_buttons(
        self,
        app
    ):

        return self.perception.find(
            app,
            role="push button"
        )

    def find_links(
        self,
        app
    ):

        return self.perception.find(
            app,
            role="link"
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



    def find_best(
        self,
        app,
        role=None,
        text=None
    ):

        elements = self.perception.observe(
            app
        )

        return self.reasoner.find_best_element(
            elements,
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


    def type(
        self,
        text
    ):

        type_text(
            text
        )

        return {
            "success": True
        }


    def press(
        self,
        key
    ):

        press_key(
            key
        )

        return {
            "success": True
        }


    def wait(
        self,
        seconds
    ):

        time.sleep(
            seconds
        )

        return {
            "success": True
        }


    def double_click(
        self,
        element
    ):

        result = self.click(
            element
        )

        if not result["success"]:
            return result

        double_click()

        return {
            "success": True
        }


    def right_click(
        self,
        element
    ):

        result = self.click(
            element
        )

        if not result["success"]:
            return result

        right_click()

        return {
            "success": True
        }


    def hover(
        self,
        element
    ):

        if element is None:

            return {
                "success": False
            }

        bounds = element["bounds"]

        move_mouse(

            bounds["x"] +
            bounds["width"] // 2,

            bounds["y"] +
            bounds["height"] // 2

        )

        return {
            "success": True
        }