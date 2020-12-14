from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        return 1234567


class Dimension(Shape):
    def __init__(self):
        self.length = 6
        self.breadth = 4

    def area(self):
        c = self.length * self.breadth
        return c


d = Dimension()
print(d.area())
