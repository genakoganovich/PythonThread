import threading
from time import sleep


def task():
    print(f"-starting task with {threading.current_thread().name}, {threading.active_count()=}")
    sleep(3)
    print(f"---end task with {threading.current_thread().name}")


task()
thr_1 = threading.Thread(target=task, daemon=True)
thr_1.start()

sleep(1)
print(f"{threading.active_count()=}")
print("END MAIN")