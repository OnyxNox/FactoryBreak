from abc import ABC

from decorators import iterable_dataclass

class Component(ABC):
    pass

@iterable_dataclass
class Color(Component):
    color: tuple[int, int, int]

@iterable_dataclass
class Name(Component):
    name: str

@iterable_dataclass
class Position(Component):
    x: float
    y: float

class Shape(Component):
    pass

@iterable_dataclass
class Circle(Shape):
    radius: float

@iterable_dataclass
class Rectangle(Shape):
    width: float
    height: float

@iterable_dataclass
class Collider(Component):
    shape: Shape

@iterable_dataclass
class Velocity(Component):
    x: float
    y: float