from modules.automation.accessibility import (
    find_application,
    find_active_document,
    get_ui_elements
)
from modules.perception.text_cleaner import TextCleaner

DOCUMENT_ROLES = {

    "document web",

    "heading",

    "paragraph",

    "text",

    "static",

    

}

class AccessibilityReader:

    def read(
        self,
        app
    ):

        application = find_application(
            app
        )

        if application is None:
            return []

        document = find_active_document(
            application
        )

        elements = get_ui_elements(
            document
        )

        text = []

        for element in elements:

            name = element["name"]

            if not name:
                continue

            name = name.strip()

            if not name:
                continue

            role = element["role"]

            if role not in DOCUMENT_ROLES:
                continue

            text.append(name)

        cleaner = TextCleaner()

        return cleaner.clean(text)