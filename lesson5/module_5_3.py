def inst(other):
    if isinstance(other, House):
        return other.number_of_floors
    elif isinstance(other, int):
        return other

class House:

    def __init__(self, name, floor):
        self.name = name
        self.number_of_floors = floor

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        return self.number_of_floors == inst(other)

    def __add__(self, value):
        self.number_of_floors += value
        return self

    def __radd__(self, other):
        return self.__add__(inst(other))

    def __iadd__(self, value):
        return self.__add__(value)

    def __gt__(self, other):
        return self.number_of_floors > inst(other)

    def __ge__(self, other):
        return self.number_of_floors >= inst(other)

    def __le__(self, other):
        return self.number_of_floors <= inst(other)

    def __lt__(self, other):
        return self.number_of_floors < inst(other)

    def __ne__(self, other):
        return self.number_of_floors != inst(other)

    def go_to(self, new_floor):
        if new_floor < 1 or new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 10 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__