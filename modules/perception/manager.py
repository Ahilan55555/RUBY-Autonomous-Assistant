from modules.automation.accessibility import (
    get_ui_elements,
    find_application
)

from modules.perception.ui_element import (
    create_ui_element
)

from modules.perception.ocr_perception import (
    observe as observe_ocr
)

INTERACTIVE_ROLES = {

    "entry",

    "push button",

    "link",

    "combo box",

    "check box",

    "toggle button",

    "slider",

    "radio button",

    "menu item",

    "list item",

    "table cell"
}

class PerceptionManager:

    def observe(
        self,
        app
    ):

        application = find_application(
            app
        )

        if application is None:

            return []

        elements = get_ui_elements(
            application
        )

        clean = []

        for element in elements:

            if element["role"] not in INTERACTIVE_ROLES:
                continue

            bounds = element["bounds"]

            if bounds is None:
                continue

            if bounds["width"] <= 0:
                continue

            if bounds["height"] <= 0:
                continue

            clean.append(

                create_ui_element(

                    source="accessibility",

                    name=element["name"],

                    role=element["role"],

                    bounds=element["bounds"],

                    states=element["states"],

                    node=element["node"]

                )

            )
        ocr = observe_ocr()

        clean.extend(
            ocr
        )

        return clean


    def find(
        self,
        app,
        role=None,
        text=None
    ):

        elements = self.observe(app)

        if role is not None:

            elements = [

                e

                for e in elements

                if e["role"] == role

            ]

        if text is not None:

            text = text.lower()

            elements = [

                e

                for e in elements

                if text in e["name"].lower()

            ]

        return elements