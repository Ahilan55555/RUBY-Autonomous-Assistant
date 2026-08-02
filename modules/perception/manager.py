from modules.automation.accessibility import (
    get_ui_elements,
    find_application,
    find_active_document
)

from modules.perception.ui_element import (
    create_ui_element
)

from modules.perception.ocr_perception import (
    observe as observe_ocr
)

from modules.perception.fusion import (
    merge
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

        active_document = find_active_document(
            application
        )

        elements = get_ui_elements(
            active_document
        )

        print("\n========== RAW UI ELEMENTS ==========")

        for e in elements:
            print(
                e["role"],
                "|",
                e["name"]
            )

        print("====================================\n")

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

        return merge(
            clean
        )


    def observe_page(
        self,
        app
    ):

        application = find_application(
            app
        )

        if application is None:
            return []

        active_document = find_active_document(
            application
        )

        elements = get_ui_elements(
            active_document
        )

        clean = []

        for element in elements:

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

        return merge(
            clean
        )


    def find(
        self,
        app,
        role=None,
        text=None
    ):

        elements = self.observe(
            app
        )

        if role is not None:

            elements = [

                element

                for element in elements

                if element["role"] == role

            ]

        if text is not None:

            text = text.lower()

            elements = [

                element

                for element in elements

                if text in element["name"].lower()

            ]

        return elements