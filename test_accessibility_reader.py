from modules.perception.accessibility_reader import (
    AccessibilityReader
)

reader = AccessibilityReader()

text = reader.read(
    "Firefox"
)

print("TOTAL:", len(text))

for line in text[:50]:
    print(line)