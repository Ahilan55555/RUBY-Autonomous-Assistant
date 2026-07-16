class TextCleaner:

    IGNORE = {

        "you said:",

        "chatgpt said:",

        "copy message",

        "edit message",

        "show more",

        "your message actions",

        "open sidebar",

        "model selector",

        "new chat",

        "skip to content",

        "open conversation options"

    }

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

            lower = line.lower()

            if lower in self.IGNORE:
                continue

            if len(line) < 3:
                continue

            if lower in seen:
                continue

            seen.add(lower)

            cleaned.append(line)

        return cleaned