import threading


def do_request(card_number: str):
    pass


# Ваше решение
card = '40070000000'
threads = []

for i in range(28, 100):
    threads.append(threading.Thread(target=do_request, args=(f'{card}{i}',), daemon=True))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join(1)
