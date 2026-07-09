class VerificationAgent:

    def text_exists(
        self,
        expected_text,
        visible_texts
    ):

        expected = expected_text.lower()

        for text in visible_texts:

            if expected in text.lower():

                return True

        return False


    def verify(
        self,
        expected_text,
        visible_texts
    ):

        return {
            "success": self.text_exists(
                expected_text,
                visible_texts
            )
        }


    def missing_text(
        self,
        expected_text,
        visible_texts
    ):

        return not self.text_exists(
            expected_text,
            visible_texts
        )


    def verify_focus(
        self,
        element
    ):

        if element is None:
            return False

        states = " ".join(
            element.get(
                "states",
                []
            )
        ).lower()

        return "focused" in states


    def verify_exists(
        self,
        element
    ):

        return element is not None


    def verify_enabled(
        self,
        element
    ):

        if element is None:
            return False

        states = " ".join(
            element.get(
                "states",
                []
            )
        ).lower()

        return "enabled" in states


    def verify_visible(
        self,
        element
    ):

        if element is None:
            return False

        states = " ".join(
            element.get(
                "states",
                []
            )
        ).lower()

        return (
            "visible" in states
            and
            "showing" in states
        )