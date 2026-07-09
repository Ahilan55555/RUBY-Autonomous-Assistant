def merge(elements):

    merged = []

    seen = set()

    for element in elements:

        key = (

            element["role"],

            element["name"].lower()

        )

        if key in seen:
            continue

        seen.add(key)

        merged.append(element)

    return merged