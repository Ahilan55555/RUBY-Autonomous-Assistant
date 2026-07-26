from modules.perception.accessibility_reader import AccessibilityReader
from modules.perception.ocr_reader import OCRReader
from modules.perception.text_fusion import TextFusion

a = AccessibilityReader().read("Firefox")
o = OCRReader().read()

fusion = TextFusion()

merged = fusion.merge(a, o)

print("Accessibility:", len(a))
print("OCR:", len(o))
print("Merged:", len(merged))

for line in merged[:50]:
    print(line)