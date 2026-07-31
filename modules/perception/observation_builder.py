from core.observation import Observation


class ObservationBuilder:

    def build(
        self,
        elements
    ):

        observation = Observation()

        observation.accessibility_tree = elements

        for element in elements:

            name = element.get(
                "name",
                ""
            )

            role = element.get(
                "role",
                ""
            ).lower()

            if not name:
                continue

            observation.visible_text.append(
                name
            )

            # Buttons
            if role in (
                "push button",
                "toggle button",
                "check box",
                "radio button",
                "menu item"
            ):

                observation.buttons.append(name)

            # Links
            elif role == "link":

                observation.links.append(name)

            # Headings
            elif role == "heading":

                observation.headings.append(name)

            # Input fields
            elif role in (
                "entry",
                "password text",
                "combo box"
            ):

                observation.inputs.append(name)

            # Everything else
            else:

                observation.page_text.append(name)


        observation.buttons = list(dict.fromkeys(observation.buttons))

        observation.links = list(dict.fromkeys(observation.links))

        observation.headings = list(dict.fromkeys(observation.headings))

        observation.inputs = list(dict.fromkeys(observation.inputs))

        observation.page_text = list(dict.fromkeys(observation.page_text))

        observation.visible_text = list(dict.fromkeys(observation.visible_text))

        return observation