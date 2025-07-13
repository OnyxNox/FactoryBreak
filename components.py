from abc import ABC
from dataclasses import dataclass

class Component(ABC):
    pass

class Collider(Component):
    pass

@dataclass
class Color(Component):
    color: tuple[int, int, int]

@dataclass
class Name(Component):
    name: str

@dataclass
class Position(Component):
    x: float
    y: float

class Shape(Component):
    pass

@dataclass
class Circle(Shape):
    radius: float

@dataclass
class Rectangle(Shape):
    width: int
    height: int

    def __iter__(self):
        yield self.width
        yield self.height

@dataclass
class Velocity(Component):
    x: float
    y: float