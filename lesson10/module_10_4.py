import queue
from random import randint
from time import sleep
from threading import Thread


class Table:

    def __init__(self, number):
        self.number = number
        self.guest = None

class Guest(Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 10))

class Cafe:

    def __init__(self, *tables):
        self.tables = tables
        self.queue = queue.Queue()

    def guest_arrival(self, *guests):
        j = 0
        for i in tables:
            g = guests[j]
            if i.guest is None:
                i.guest = g
                j += 1
                print(f"{i.guest.name} сел(-а) за стол номер {i.number}")
            else:
                self.queue.put(g)
                print(f"{g.name} в очереди")
        for i in range(j, len(guests)):
            self.queue.put(guests[j])
            j += 1

    def discuss_guests(self):
        while True:
            for i in self.tables:
                if i.guest is not None and not i.guest.is_alive():
                    print(f"{i.guest.name} покушал(-а) и ушёл(ушла)")
                    print(f"Стол номер {i.number} свободен")
                    i.guest = None
                    if not self.queue.empty() and i.guest is None:
                        i.guest = self.queue.get()
                        print(f"{i.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {i.number}")
                        i.guest.start()
            if self.queue.empty() and not any([i.guest for i in self.tables]):
                break

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