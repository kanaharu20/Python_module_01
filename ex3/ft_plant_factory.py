#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self._name = name
        self._height = height
        self._ages = ages

    def show(self) -> None:
        print(f"{self._name}: {round(self._height,1)}cm, {self._ages} days old")

    def grow(self) -> None:
        self._height += 0.4

    def age(self) -> None:
        self._ages += 1


def ft_plant_factory() -> None:
    print("=== Plant Factory Output ===")
    Rose = Plant("Rose", 25.0, 30)
    Oak = Plant("Oak", 200.0, 365)
    Cactus = Plant("Cactus", 5.0, 90)
    Sunflower = Plant("Sunflower", 80.0, 45)
    Fern = Plant("Fern", 15.0, 120)
    for plant in [Rose, Oak, Cactus, Sunflower, Fern]:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    ft_plant_factory()
