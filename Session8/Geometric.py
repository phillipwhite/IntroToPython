class GeometricObject:
    def __init__(self, colour:str = "white", filled:bool = False):
        self.colour = colour
        self.filled = filled

    def getColour(self):
        return self.colour

    def setColour(self, colour:str):
        self.colour = colour


class Circle(GeometricObject):

    def __init__(self, colour:str = "white", filled:bool = False,
                 radius:float = 1):
        super.__init__(colour, filled)
        self.radius = radius



ob1 = GeometricObject()
ob2 = GeometricObject("blue", True)

circ1 = Circle("blue", True, 3)


