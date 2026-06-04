#!/usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self._name = name
        self._height = height
        self._ages = ages

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height,1)}cm, "
            f"{self._ages} days old"
        )

    def grow(self) -> None:
        self._height += 0.4

    def age(self) -> None:
        self._ages += 1


def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    Rose = Plant("Rose", 25.0, 30)
    Rose.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        Rose.grow()
        Rose.age()
        Rose.show()
    print(f"Growth this week: {round(Rose._height - 25,1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
