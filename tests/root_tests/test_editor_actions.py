from modules.actions.editor_actions import (
    write_file,
    append_file
)

write_file(
    "hello.txt",
    "Hello\n"
)

append_file(
    "hello.txt",
    "World\n"
)

print(
    open(
        "hello.txt"
    ).read()
)