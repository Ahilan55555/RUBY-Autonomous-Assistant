from modules.perception.page_reader import PageReader

reader = PageReader()

text = reader.read(
    "Firefox"
)

print(text)