#When we want to provide a common interface for different implementations of a component, we use an abstract class. 

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

rect1 = Rectangle(2,3)
print(rect1.area())