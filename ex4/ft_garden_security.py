#! /usr/bin/env python3

class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self._name = name
        self._height = height
        self._ages = ages

    def show(self) -> None:
        print(f"{self._name}: {self._height:.1f}cm, ", end="")
        print(f"{self._ages} days old")

    def get_height(self) -> float:
        return round(self._height, 1)

    def get_age(self) -> int:
        return (self._ages)

    def set_height(self, height: float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        self._height = height
        print(f"Height updated: {self.get_height()}cm")

    def set_age(self, ages: int) -> None:
        if ages < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        self._ages = ages
        print(f"Age updated: {self.get_age()} days")


def ft_garden_security() -> None:
    print("=== Garden Security System ===")
    Rose = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    Rose.show()
    print()
    Rose.set_height(25)
    Rose.set_age(30)
    print()
    Rose.set_height(-1)
    Rose.set_age(-1)
    print()
    print("Current state: ", end="")
    Rose.show()


if __name__ == "__main__":
    ft_garden_security()