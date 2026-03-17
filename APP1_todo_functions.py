from pathlib import Path

# This sets the path to "todos.txt" in the SAME folder as this file
FILEPATH = Path(__file__).parent / "todos.txt"


def get_todos():
    """Reads the todo items from the text file."""
    if not FILEPATH.exists():
        FILEPATH.write_text("")  # create file if it doesn't exist

    with open(FILEPATH, "r") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg):
    """Writes the todo items list to the text file."""
    with open(FILEPATH, "w") as file:
        file.writelines(todos_arg)
