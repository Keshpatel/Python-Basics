class Car:
    # class variable
    Wheels = 4

    # constuctor of this class:
    def __init__(self):
        print("Default constructor")

    def __init__(self, color):
        print("Car Class constructor")
        self.color = color

    def test(self):
        print("Test Method")

    # if any var is declared inside the method of contructor :instance variable
    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

# how to create an object of this class:
c1 = Car("Red")
print(c1.Wheels)
print(Car.Wheels)

c1.test()
c1.setPrice(1000)
print(c1.getPrice())

c2 = Car("Black")
c2.setPrice(3000)
print(c2.getPrice())

class TEst:
    a = 10

# Blank class
class BlankClass:
    pass

p1 = BlankClass()



