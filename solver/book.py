from dataclasses import dataclass


@dataclass
class Book:
    name: str
    x: int
    y: int
    direction: str

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name

    def __repr__(self) -> str:
        return f"{self.name} at ({self.x}, {self.y})"
