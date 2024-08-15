import threading
import time
import random
import queue


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(threading.Thread):
    def __init__(self, *name):
        super().__init__()
        self.name = name

    def run(self):
        sl = random.randint(3, 10)
        time.sleep(sl)


class Cafe:
    def __init__(self, *tables_):
        self.tables = tables_
        self.queue = queue.Queue()

    def guest_arrival(self, *quests):
        for guest in guests:
            assigned = False
            for table in self.tables:
                if table.guest is None:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}")
                    assigned = True
                    break
            if not assigned:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        while not self.queue.empty() or any(table.guest is not None for table in self.tables):
            for table in self.tables:
                if table.guest is not None and not table.guest.is_alive():
                    print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {table.number} свободен")
                    table.guest = None

                if table.guest is None and not self.queue.empty():
                    guest_from_queue = self.queue.get()
                    table.guest = guest_from_queue
                    table.guest.start()
                    print(f"{guest_from_queue.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")


# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
