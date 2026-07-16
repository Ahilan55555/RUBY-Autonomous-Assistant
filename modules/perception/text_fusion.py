class TextFusion:

    def merge(
        self,
        accessibility_text,
        ocr_text
    ):

        merged = []

        seen = set()

        for source in (
            accessibility_text,
            ocr_text
        ):

            for line in source:

                key = line.lower()

                if key in seen:
                    continue

                seen.add(key)

                merged.append(line)

        return merged