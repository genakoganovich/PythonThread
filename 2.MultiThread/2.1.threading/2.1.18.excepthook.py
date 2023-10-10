import threading
from time import sleep


def task():
    sleep(0.5)
    raise Exception("!!! exception in task !!!")


thread_1 = threading.Thread(target=task)
thread_1.start()
