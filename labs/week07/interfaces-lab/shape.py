from abc import ABC, abstractmethod
import math



class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return math.pi * self.radius**2



class Square(Shape):
    def __init__(self, length):
        self.length = length


    def area(self):
        return self.length**2



def print_area(shape):
    print(shape.area())



c = Circle(5)
s = Square(5)

print_area(c)
print_area(s)