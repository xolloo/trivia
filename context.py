from contextlib import suppress
from contextlib import redirect_stdout
from contextlib import ExitStack
from datetime import datetime
import os

try:
    with open("file.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("File not found.")


with suppress(FileNotFoundError):
    with open("file.txt", "r") as file:
        print(file.read())


path = "file.txt"
with open(path, "w") as file:
    with redirect_stdout(file):
        help(redirect_stdout)
        print(dir(redirect_stdout))
        print(datetime.utcnow())

filenames = os.listdir(".venv/bin")

with ExitStack() as stack:
    file_objects = [
        stack.enter_context(open(filename))
        for filename in filenames
        if os.path.isfile(filename)
    ]

    for file in file_objects:
        print(file)
