class BMI:

    def __init__(self, name: str, weight: float, height: float, age: int = 20):
        self.name = name
        self.age = age
        self. weight = weight
        self.height = height

    def getBMI(self):
        return self.weight / (self.height * self.height) * 703

    def getStatus(self):
        if self.getBMI() < 18.5:
            return "Underweight"
        elif self.getBMI() < 24.9:
            return "Healthy Weight"
        elif self.getBMI() < 29.9:
            return "Overweight"
        else:
            return "Obesity"



philBMI = BMI("Phil", 66.6 * 2.2, 67, 66)
print(philBMI.getBMI())
print(philBMI.getStatus())


