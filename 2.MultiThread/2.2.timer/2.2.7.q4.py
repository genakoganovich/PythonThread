from threading import Timer
from time import sleep


def worker(task: str):
    sleep(2)
    print(f"{task=} done")


# timer = Timer(1, worker, "print")
# timer.start()


# timer = Timer(1, worker, args=("print", ))
# timer.start()

# timer = Timer(interval=1, function=worker, args=("print", ), name="new_timer")
# timer.start()

# timer = Timer(interval=1, function=worker(), args=("print", ))
# timer.name = "new_timer"
# timer.start()

# Timer(1.0, worker, ["print"]).start()


# timer = Timer(interval=1, worker, args=("print", ))
# timer.name = "new_timer"
# timer.start()
