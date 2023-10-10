import threading
import time


def test():
    print(f"{threading.current_thread().name} started")


timer = threading.Timer(2, function=test)
timer.start()
time.sleep(2)
timer.cancel()  # может произойти а может и нет. Время отложенного запуска и пауза до отмены совпадают!!
