#! /usr/bin/env python3

class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        ages: int
    ) -> None:
        self._name = name
        self._height = height
        self._ages = ages


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        color: str,
        status: bool
    ) -> None:
        super().__init__(name, height, ages)
        self._color = color
        self._status = status

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._ages} days old\n Color: {self._color}"
            )
        if self._status:
            print(f" {self._name} is blooming beautifully!")
        else:
            print(f" {self._name} has not bloomed yet")
            print(f"[asking the {self._name} to bloom]")

    def bloom(self) -> None:
        self._status = True


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        trunk_diameter: float
    ) -> None:
        super().__init__(name, height, ages)
        self._trunk_diameter = trunk_diameter

    def show(self) -> None:
        print(
            f"{self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._ages} days old\n"
            f" Trunk diameter: {self._trunk_diameter}cm"
        )

    def produce_shade(self) -> None:
        print(f"[asking the {self._name} to produce shade]")
        print(f"Tree {self._name} now produces a shade of {self._height}cm long and {self._trunk_diameter}cm wide.")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: float,
        ages: int,
        harvest_season: str,
        nutritional_value: int
    ) -> None:
        super().__init__(name, height, ages)
        self._harvest_season = harvest_season
        self._nutritional_value = nutritional_value

    def age(self) -> None:
        self._ages += 20

    def grow(self) -> None:
        self._height += 42

    def add_nut(self) -> None:
        self._nutritional_value += 20

    def show(self) -> None:
        print(
            f"{self._name}: "
            f"{round(self._height, 1)}cm, "
            f"{self._ages} days old"
            )
        print(
            f" Harvest season: {self._harvest_season}\n"
            f" Nutritional value: "
            f"{self._nutritional_value}"
            )


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red", False)
    Rose.show()
    Rose.bloom()
    Rose.show()
    print("")

    print("=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    Oak.produce_shade()
    print("")

    print("=== Vegetable")
    Tomato = Vegetable("Tomato", 5.0, 10, "April", 0)
    Tomato.show()
    print("[make Tomato grow and age for 20 days]")
    Tomato.age()
    Tomato.grow()
    Tomato.add_nut()
    Tomato.show()


if __name__ == "__main__":
    ft_plant_types()
