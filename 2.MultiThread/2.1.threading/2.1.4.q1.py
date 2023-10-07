import threading


def add(a, b):
    print(a + b)


# thr = threading.Thread(target=add, args=(1, 2), name="new_name")
# thr.start()

# threading.Thread(target=add, args=(1, 2), name="new_name").start()

# thr = threading.Thread(target=add(), args=(1, 2))
# thr.start()

# thr = threading.Thread(add, args=(1, 2))
# thr.name = "new_name"
# thr.start()

# thr = threading.Thread(target=add, args=(1, 2)).start()
# thr.name = "new_name"

# thr = threading.Thread(add, 1, 2)
# thr.start()
