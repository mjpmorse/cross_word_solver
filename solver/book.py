from dataclasses import dataclass


@dataclass
class Book:
    name: str
    x: int
    y: int
    direction: str

    def __eq__(self, __o: object) -> bool:
        cond = (
            (self.name.upper() == __o.name.upper()) and
            (self.direction == __o.direction) and
            (self.x == __o.x) and
            (self.y == __o.y)
        )
        return cond
