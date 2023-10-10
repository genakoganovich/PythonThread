from threading import Thread, Timer, current_thread
from time import sleep


def executer():
    sleep(0.1)
    print("work done")


def logging():
    print(f"{current_thread().name} logging")


thread = Thread(target=executer, daemon=True)
timer = Timer(0.1, logging)

thread.start()
timer.start()

thread.join(0.1)  # добавили таймаут
timer.cancel()
timer.join()
