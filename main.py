class House:
    def __init__(self,name,number_of_floors):
        self.name=name
        self.number_of_floor = number_of_floors
    def go_to(self,new_floor):
        floor=0
        if new_floor > self.number_of_floor:
            print("такого этажа нет")
        else:
            for i in range(new_floor):

                floor = floor + 1
                print(floor)
    def __len__(self):
        return self.number_of_floor
    def __str__(self):
        return f"Название:{self.name}, Кол-во этажей {self.number_of_floor} "
    def __lt__(self, other):
        return self.number_of_floor < other.number_of_floor

    def __eq__(self, other):
        return self.number_of_floor == other.number_of_floor

    def __le__(self, other):
        return self.number_of_floor <= other.number_of_floor

    def __gt__(self, other):
        return self.number_of_floor > other.number_of_floor

    def __ge__(self, other):
        return self.number_of_floor >= other.number_of_floor

    def __ne__(self, other):
        return self.number_of_floor != other.number_of_floor
    def __add__(self, other):
        return self.number_of_floor + other
    def __iadd__(self, other):
        return self.number_of_floor + other
    def __radd__(self, other):
        return self.number_of_floor + other

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
