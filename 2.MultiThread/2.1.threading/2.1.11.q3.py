import threading


def test():
    print()


thr_1 = threading.Thread(target=test, daemon=True)
thr_1.start()
thr_1.join(timeout=2)
