class Pet():
    pass

class Animals(Pet):
    pass

class Dog(Animals):
    @staticmethod
    def bark ():
        print(" Bow bow")



a = Dog()
a.bark()   #output:    bow bow
