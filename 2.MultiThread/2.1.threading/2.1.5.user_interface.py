import threading
import time


def user_interface():
    while True:
        time.sleep(0.2)
        print("-", end="")


def task():
    while True:
        time.sleep(0.61)
        print("*", end="")


func = [task, user_interface]
for f in func:
    threading.Thread(target=f).start()
