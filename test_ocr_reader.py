from modules.perception.ocr_reader import (
    OCRReader
)

reader = OCRReader()

text = reader.read()

print("TOTAL:", len(text))

for line in text[:50]:
    print(line)