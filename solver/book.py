from dataclasses import dataclass


@dataclass
class Book:
    def __init__(
        self,
        name: str,
        x_coord: int,
        y_coord: int,
        direction: str
    ) -> None:
        self.name = name
        self.x = x_coord
        self.y = y_coord
        self.direction = direction

    def __eq__(self, __o: object) -> bool:
        return self.name == __o.name

    def __repr__(self) -> str:
        return f"{self.name} at ({self.x}, {self.y})"
