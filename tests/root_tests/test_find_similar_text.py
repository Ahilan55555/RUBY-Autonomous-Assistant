from modules.vision.ocr import (
    find_similar_text
)

texts = [

    "ChatGPT",

    "Ask anything",

    "What is robotics?"
]

print(

    find_similar_text(
        "Ask",
        texts
    )

)