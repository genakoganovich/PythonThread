import threading
from time import perf_counter as pc


def test():
    print(f"{threading.current_thread().name} started")


t_thr = threading.Timer(2, function=test)

start_time = pc()
t_thr.start()
print(f"{threading.current_thread().name} not blocked")
t_thr.join()
print(f"after {pc() - start_time:.2f} sec.")

# MainThread not blocked
# Thread-1 started
# after 2.01 sec.
