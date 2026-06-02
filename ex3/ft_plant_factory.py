#!/usr/bin/env python3

class Plant:
    def __init__(self, _name: str, _height: float, _ages: int) -> None:
        self.name = _name
        self.height = _height
        self.ages = _ages

    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.ages} days old")

    def grow(self) -> None:
        self._height += 0.4

    def age(self) -> None:
        self._ages += 1


Rose = Plant("Rose", 25.0, 30)
Oak = Plant("Oak", 200.0, 365)
Cactus = Plant("Cactus", 5.0, 90)
Sunflower = Plant("Sunflower", 80.0, 45)
Fern = Plant("Fern", 15.0, 120)


def ft_plant_factory() -> None:
    Rose.show()
    Oak.show()
    Cactus.show()
    Sunflower.show()
    Fern.show()


if __name__ == "__main__":
    ft_plant_factory()
