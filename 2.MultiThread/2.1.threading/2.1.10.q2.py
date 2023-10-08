import threading


def test():
    print()


thr_1 = threading.Thread(target=test)
thr_1.start()
thr_1.join()
