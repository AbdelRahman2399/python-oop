# BaseClass

from abc import ABC, abstractmethod
import math

class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphicShape):
    def __init__(self,radius):
        super().__init__()
        self.radius = radius

    def calcArea(self):
        return math.pi*(self.radius**2)

c1 = Circle(10)
print(c1.calcArea())