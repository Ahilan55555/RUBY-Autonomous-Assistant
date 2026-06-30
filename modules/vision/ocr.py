import cv2
import pytesseract


def read_screen_text(image_path):

    image = cv2.imread(
        image_path
    )

    if image is None:

        return ""

    text = pytesseract.image_to_string(
        image
    )

    return text




def read_screen_boxes(image_path):

    image = cv2.imread(
        image_path
    )

    if image is None:

        return []

    data = pytesseract.image_to_data(
        image,
        output_type=
        pytesseract.Output.DICT
    )

    results = []

    for i in range(
        len(data["text"])
    ):

        text = data["text"][i].strip()

        if not text:
            continue

        results.append(
            {
                "text": text,
                "x": data["left"][i],
                "y": data["top"][i],
                "w": data["width"][i],
                "h": data["height"][i]
            }
        )

    return results

def contains_text(
    image_path,
    target_text
):

    text = read_screen_text(
        image_path
    )

    return (
        target_text.lower()
        in text.lower()
    )

def get_visible_texts(
    image_path
):

    boxes = read_screen_boxes(
        image_path
    )

    return [

        box["text"]

        for box in boxes

        if box["text"].strip()
    ]

def get_visible_texts(image_path):

    boxes = read_screen_boxes(
        image_path
    )

    return [
        box["text"]
        for box in boxes
        if box["text"].strip()
    ]

def find_similar_text(
    expected_text,
    visible_texts
):

    expected = expected_text.lower()

    for text in visible_texts:

        if expected in text.lower():

            return text

    return None