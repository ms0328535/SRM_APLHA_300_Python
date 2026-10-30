class Suppress:
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is ZeroDivisionError:
            print("Caught:", exc_value)
            return True               # swallow this error only
        return False                  # other errors propagate

with Suppress():
    print(1 / 0)
print("program continues")

# Standard library equivalent
from contextlib import suppress
with suppress(FileNotFoundError):
    open("missing.txt")