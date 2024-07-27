class GeometricObject:
    def __init__(self, colour:str = "white", filled:bool = False):
        self.colour = colour
        self.filled = filled

    def getColour(self):
        return self.colour

    def setColour(self, colour:str):


ob1 = GeometricObject()
ob2 = GeometricObject("blue", True)
