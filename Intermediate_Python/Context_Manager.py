# Without a context manager (easy to forget close, breaks on errors)
f = open("notes.txt", "w")
try:
    f.write("hello")
finally:
    f.close()

# With a context manager (cleanup is automatic)
with open("notes.txt", "w") as f:
    f.write("hello")
print(f.closed)    # True


# Multiple resources in one with
with open("in.txt") as src, open("out.txt", "w") as dst:
    dst.write(src.read().upper())

# Locks (threading)
from threading import Lock
lock = Lock()
with lock:
    pass   # lock is released automatically

# Temporary directory, deleted afterwards
import tempfile
with tempfile.TemporaryDirectory() as tmp:
    print("working in", tmp)

# Database connection (commit or rollback automatically)
import sqlite3
with sqlite3.connect(":memory:") as conn:
    conn.execute("CREATE TABLE t (x INT)")
    conn.execute("INSERT INTO t VALUES (1)")

# Decimal precision for a block
from decimal import Decimal, localcontext
with localcontext() as ctx:
    ctx.prec = 5
    print(Decimal(1) / Decimal(3))


class FileManager:
    def __init__(self, path, mode):
        self.path = path
        self.mode = mode
        self.file = None

    def __enter__(self):
        print("Opening file")
        self.file = open(self.path, self.mode)
        return self.file              # this becomes the `as` variable

    def __exit__(self, exc_type, exc_value, traceback):
        print("Closing file")
        if self.file:
            self.file.close()
        # Return True to suppress the exception, False/None to let it propagate
        return False

with FileManager("demo.txt", "w") as f:
    f.write("Hello")



    