class Animal:
    def __init__(self, order):
        self.order = order


class Dog(Animal):
    def __init__(self, order):
        Animal.__init__(self, order)


class Cat(Animal):
    def __init__(self, order):
        Animal.__init__(self, order)


class AnimalShelter:
    def __init__(self):
        self.dogsList = []
        self.catsList = []
        self.order = 0

    def enqueue(self, animal):
        order += 1
        if isinstance(animal, Dog):
            self.dogsList.append(animal)
        elif isinstance(animal, Cat):
            self.catsList.append(animal)

    def dequeueAny(self):
        if len(self.dogsList) == 0:
            return self.dequeueCat()
        elif len(self.catsList) == 0:
            return self.dequeueDog()
        dog = self.dogsList[0]
        cat = self.catsList[0]
        if dog.order < cat.order:
            return self.dequeueDog()
        else:
            return self.dequeueCat()

    def dequeueDog(self):
        dog = None
        if len(self.dogsList) != 0:
            dog = self.dogsList.pop(0)
        return dog

    def dequeueCat(self):
        cat = None
        if len(self.cagtsList) != 0:
            cat = self.catsList.pop(0)
        return cat

    




