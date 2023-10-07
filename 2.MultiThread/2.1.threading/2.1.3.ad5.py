import threading


def task(function, *args, **kwargs):
    print(f"{'started_task':-^70}")
    print(f"{threading.current_thread().name=}, {threading.active_count()=}")
    function(*args, **kwargs)
    print(f"{'end_task':-^70}")


task(print, "здесь могла быть ваша реклама")

tasks = []
for i in range(5):
    tasks.append(threading.Thread(target=task, args=(print, f"просто текст №{i}")))

for task in tasks:
    task.start()