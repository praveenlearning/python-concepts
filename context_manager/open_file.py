import os
from contextlib import contextmanager


class OpenFile:

    def __init__(self, filename: str, mode: str):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    yield file
    file.close()


with OpenFile("some.txt", 'a') as f:
    f.write("Python is awesome\n")

print(f.closed)

with open_file("some.txt", "a") as f:
    f.write("Python awesome again\n")

print(f.closed)

os.makedirs("Sample-Dir-One", exist_ok=True)
os.makedirs("Sample-Dir-Two", exist_ok=True)

cwd = os.getcwd()
os.chdir('Sample-Dir-One')
print(os.listdir())
os.chdir(cwd)

cwd = os.getcwd()
os.chdir('Sample-Dir-Two')
print(os.listdir())
os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


print('With contextmanager')
with change_dir("Sample-Dir-One"):
    print(os.listdir())

with change_dir("Sample-Dir-Two"):
    print(os.listdir())
