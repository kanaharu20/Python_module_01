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


def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    Rose = Plant("Rose", 25, 30)
    Sunflower = Plant("Sunflower", 80, 45)
    Cactus = Plant("Cactus", 15, 120)
    Rose.show()
    Sunflower.show()
    Cactus.show()


if __name__ == "__main__":
    ft_garden_data()
