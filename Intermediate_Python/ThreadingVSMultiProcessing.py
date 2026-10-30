# Threads: share memory, good for I/O-bound work (network, files, waiting)
# Processes: separate memory, good for CPU-bound work (heavy calculations)
# The GIL lets only one thread run Python bytecode at a time,
# so threads don't speed up CPU-heavy code.

import time
from threading import Thread
from multiprocessing import Process

def cpu_task(n=5_000_000):
    total = 0
    for i in range(n):
        total += i * i

def timed(label, runner):
    start = time.time()
    runner()
    print(f"{label}: {time.time() - start:.2f}s")

def run_threads():
    ts = [Thread(target=cpu_task) for _ in range(4)]
    [t.start() for t in ts]; [t.join() for t in ts]

def run_processes():
    ps = [Process(target=cpu_task) for _ in range(4)]
    [p.start() for p in ps]; [p.join() for p in ps]

if __name__ == "__main__":
    timed("4 threads", run_threads)        # about as slow as sequential
    timed("4 processes", run_processes)    # noticeably faster on multi-core