from datetime import datetime


class Observation:

    def __init__(self):

        self.success = True

        self.window_title = None

        self.window_id = None

        self.url = None

        self.page_title = None

        self.page_text = []

        self.buttons = []

        self.links = []

        self.headings = []

        self.inputs = []

        self.visible_text = []

        self.ocr_text = None

        self.accessibility_tree = None

        self.timestamp = datetime.now()

    def __repr__(self):

        return (

            "Observation("

            f"url={self.url}, "

            f"title={self.page_title}"

            ")"

        )