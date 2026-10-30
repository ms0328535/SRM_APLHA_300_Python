import time
from threading import Thread, Lock, Event, current_thread
from queue import Queue
from concurrent.futures import ThreadPoolExecutor

# Basic thread with arguments
def worker(name, delay):
    time.sleep(delay)
    print(f"{name} done in {current_thread().name}")

t = Thread(target=worker, args=("task-1", 1))
t.start()
t.join()                                   # wait for it to finish

# Race condition fixed with a Lock
balance = 0
lock = Lock()

def deposit():
    global balance
    for _ in range(100_000):
        with lock:
            balance += 1

threads = [Thread(target=deposit) for _ in range(5)]
[t.start() for t in threads]; [t.join() for t in threads]
print(balance)                             # 500000

# Producer/consumer with Queue
q = Queue()

def producer():
    for i in range(5):
        q.put(i)
    q.put(None)                            # sentinel to stop

def consumer():
    while (item := q.get()) is not None:
        print("got", item)
        q.task_done()

Thread(target=producer).start()
c = Thread(target=consumer); c.start(); c.join()

# Daemon threads exit when the main program exits
Thread(target=lambda: time.sleep(100), daemon=True).start()

# Easiest modern way: ThreadPoolExecutor
def fetch(n):
    time.sleep(0.5)
    return n * 2

with ThreadPoolExecutor(max_workers=4) as ex:
    print(list(ex.map(fetch, range(8))))