import copy

orig = [[1, 2], [3, 4]]
shallow = copy.copy(orig)
deep = copy.deepcopy(orig)

orig[0].append(99)
print(shallow[0])   # [1, 2, 99] (inner list is shared)
print(deep[0])      # [1, 2]     (fully independent)

# Custom context manager that times a block
import time
class Timer:
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__(self, exc_type, exc, tb):
        print(f"Elapsed: {time.time() - self.start:.3f}s")
        return False          # don't swallow exceptions

with Timer():
    sum(range(1_000_000))

# Generator-based version
from contextlib import contextmanager

@contextmanager
def cd_message(label):
    print(f"start {label}")
    try:
        yield
    finally:
        print(f"end {label}")

with cd_message("demo"):
    print("inside")