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