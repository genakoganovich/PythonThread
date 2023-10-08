import requests
import threading
from time import perf_counter

sources = ["https://ya.ru",
           "https://www.bing.com",
           "https://www.google.ru",
           "https://www.yahoo.com",
           "https://mail.ru"]

headers_stor = {}  # Храним здесь заголовки
start = perf_counter()
sum_ex_time = 0


def test(src):
    global headers_stor
    global start
    global sum_ex_time
    start_tmp = perf_counter()
    headers_stor[src] = requests.get(src).headers  # получаем заголовки и формируем словарь
    delta = perf_counter() - start_tmp
    print(source, delta)
    sum_ex_time += delta


threads = []

for source in sources:
    threads.append(threading.Thread(target=test, args=(source,)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(f"completed in {perf_counter() - start} seconds")  # Считаем общее время выполнения всех запросов
print(sum_ex_time)  # Показываем то, что общее время работы является простой суммой каждого запроса по отдельности
print(*headers_stor.items(), sep="\n")  # Выводим наши заголовки
