from dataclasses import dataclass, fields

def iterable_dataclass(cls):
    cls = dataclass(cls)
    def __iter__(self):
        for field in fields(self):
            yield getattr(self, field.name)
    cls.__iter__ = __iter__
    return cls