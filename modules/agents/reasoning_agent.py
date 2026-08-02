TEXT_INPUT_ROLES = {

    "entry",

    "combo box"

}



class ReasoningAgent:

    def find_best_element(
        self,
        elements,
        role=None,
        text=None
    ):

        candidates = elements

        if role == "text_input":

            candidates = [

                e

                for e in candidates

                if e["role"] in TEXT_INPUT_ROLES

            ]

        elif role is not None:

            candidates = [

                e

                for e in candidates

                if e["role"] == role

            ]

        if text is not None:

            text = text.lower()

            candidates = [

                e

                for e in candidates

                if text in e["name"].lower()

            ]

        best = None

        best_score = -1

        print("\n========== CANDIDATES ==========")

        for e in candidates:
            print(
                e["role"],
                " | ",
                e["name"]
            )

        print("===============================\n")

        for element in candidates:

            score = 0

            bounds = element["bounds"]

            states = " ".join(
                element["states"]
            ).lower()

            name = element["name"].lower()

            if "visible" in states:
                score += 10

            if "showing" in states:
                score += 10

            if "enabled" in states:
                score += 10

            if "editable" in states:
                score += 10

            if "focused" in states:
                score += 20

            if bounds["width"] > 300:
                score += 5

            if bounds["height"] > 20:
                score += 5

            if bounds["y"] < 300:
                score += 5

            # ----------------------------------
            # Semantic Scoring
            # ----------------------------------

            if role == "text_input":

                if "search" in name:
                    score += 100

                if "search youtube" in name:
                    score += 100

                if "address" in name:
                    score += 80

                if "url" in name:
                    score += 80

                if "chat with chatgpt" in name:
                    score -= 200

                if "chatgpt" in name:
                    score -= 200

                if "prompt" in name:
                    score -= 100

                if "message" in name:
                    score -= 100

            print(
                f"{element['name']} -> {score}"
            )

            if score > best_score:

                best_score = score

                best = element

        return best


    def find_best_textbox(
        self,
        elements
    ):

        return self.find_best_element(
            elements,
            role="entry"
        )


    def find_best_button(
        self,
        elements,
        text=None
    ):

        return self.find_best_element(
            elements,
            role="push button",
            text=text
        )


    def find_best_link(
        self,
        elements,
        text=None
    ):

        return self.find_best_element(
            elements,
            role="link",
            text=text
        )