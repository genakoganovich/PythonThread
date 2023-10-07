import threading


def task(function, *args, **kwargs):
    print(f"{'started_task':-^70}")
    print(f"{threading.current_thread().name=}, {threading.active_count()=}")
    function(*args, **kwargs)
    print(f"{'end_task':-^70}")
    print(f"{'':-^10}")


task(print, "здесь могла быть ваша реклама")
