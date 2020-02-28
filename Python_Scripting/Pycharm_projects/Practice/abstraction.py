from abc import ABC,abstractmethod

class Animal(ABC):
    count = 0

    def __init__(self):
        Animal.count += 1
        print("Animal class instatiated")

    @abstractmethod
    def eats(self):
        pass

class Tiger(Animal):
    def eats(self):
        print("Eats non veg")

class Cow(Animal):
    def eats(self):
        print("Eats veg")


tiger = Tiger()
tiger.eats()

cow = Cow()
cow.eats()