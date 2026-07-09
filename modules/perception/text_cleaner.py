class TextCleaner:

    def clean(
        self,
        lines
    ):

        cleaned = []

        seen = set()

        for line in lines:

            line = line.strip()

            if not line:
                continue

            if len(line) < 2:
                continue

            if line.lower() in seen:
                continue

            seen.add(
                line.lower()
            )

            cleaned.append(
                line
            )

        return cleaned