import math
class Circle:
    #Construct a circle object
    def __init__(self, radius = 10):
        self.__radius = radius

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * self.__radius ** 2

    def setRadius(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

circle1 = Circle()
circle2 = Circle(2)


print(circle2.getRadius())
print(circle2.getPerimeter())
print(circle2.getArea())

circle10 = Circle()
circle100 = Circle(100)
print(circle10.getArea())
print(circle100.getArea())
