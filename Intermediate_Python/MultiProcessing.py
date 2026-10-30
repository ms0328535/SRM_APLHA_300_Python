from multiprocessing import Process, Value, Array, Lock, Queue, Pool
from concurrent.futures import ProcessPoolExecutor
import os

# Shared memory with Value and a Lock
def add(counter, lock):
    for _ in range(1000):
        with lock:
            counter.value += 1

if __name__ == "__main__":                 # required, especially on Windows/macOS
    counter = Value("i", 0)
    lock = Lock()
    procs = [Process(target=add, args=(counter, lock)) for _ in range(4)]
    [p.start() for p in procs]; [p.join() for p in procs]
    print(counter.value)                   # 4000

    # Shared array
    arr = Array("d", [1.0, 2.0, 3.0])

    # Queue for passing data between processes
    def squarer(q, n):
        q.put(n * n)

    q = Queue()
    ps = [Process(target=squarer, args=(q, i)) for i in range(4)]
    [p.start() for p in ps]; [p.join() for p in ps]
    print(sorted(q.get() for _ in range(4)))

    # Pool: split work across CPU cores
    def heavy(n): return sum(i * i for i in range(n))

    with Pool(processes=4) as pool:
        print(pool.map(heavy, [10**5, 10**6, 10**6]))
        print(pool.apply(heavy, args=(1000,)))

    # Modern alternative
    with ProcessPoolExecutor() as ex:
        print(list(ex.map(heavy, [10**5, 10**5])))