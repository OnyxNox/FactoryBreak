from abc import ABC

class Component(ABC):
    pass

class Color(Component):
    def __init__(self, color: tuple[int, int, int]):
        self.color = color

class Name(Component):
    def __init__(self, name: str):
        self.name = name

class Position(Component):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y