#Multiple Inheritance/Interface

from abc import ABC, abstractmethod
import math

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape, JSONify):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return math.pi*(self.radius**2)

    def toJSON(self):
        return f'{{\' circle\' : {str(self.calcArea())} }}'

c1 = Circle(10)
print(c1.calcArea())
print(c1.toJSON())