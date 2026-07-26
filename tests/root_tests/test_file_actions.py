from modules.actions.file_actions import (
    create_file,
    create_folder
)

create_folder(
    "test_folder"
)

create_file(
    "test_folder/test.txt"
)

print(
    "done"
)