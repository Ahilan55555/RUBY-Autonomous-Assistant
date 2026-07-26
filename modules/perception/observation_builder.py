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

            if "button" in role:

                observation.buttons.append(
                    name
                )

            elif "link" in role:

                observation.links.append(
                    name
                )

            elif "heading" in role:

                observation.headings.append(
                    name
                )

            elif (
                "entry" in role
                or
                "text" in role
            ):

                observation.inputs.append(
                    name
                )

            else:

                observation.page_text.append(
                    name
                )

        return observation