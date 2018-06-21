import os
import tempfile


class File:
    def __init__(self, path):
        self.path = path
        with open(path, "a+") as f:
            f.seek(0)
            self.file_lines = f.readlines()
            self.current = 0

    def write(self, string):
        with open(self.path, "w") as f:
            f.write(string)

    def __add__(self, other):
        storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

        with open(storage_path, "w") as fsum:
            fsum.writelines(self.file_lines + other.file_lines)
        return File(storage_path)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= len(self.file_lines):
            raise StopIteration
        self.current += 1
        return self.file_lines[self.current - 1]

    def __str__(self):
        return '{}'.format(self.path)
