#! /usr/bin/env python3

class Plant:
    def __init__(self, _name: str, _height: float, _ages: int) -> None:
        self._name = _name
        self._height = _height
        self._ages = _ages

class Flower(Plant):
    def __init__(self, _name: str, _height: float, _ages: int, _color: str, _status: bool):
        super().__init__(_name, _height, _ages)
        self._color = _color
        self._status = _status

    def show(self) -> None:
        if self._status == True:
            print(
                f"{self._name}: {round(self._height, 1)}cm, {self._ages} days old\n _color: {self._color}")
            print(f" {self._name} is blooming beautifully!")
        else:
            print("[asking the rose to bloom]")

    def bloom(self) -> None:
        self._status = True


class Tree(Plant):
    def __init__(self, _name: str, _height: float, _ages: int, _trunk_diameter: float):
        super().__init__(_name, _height, _ages)
        self._trunk_diameter = _trunk_diameter

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._ages} days old\n Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")


class Vegetable(Plant):
    def __init__(self, _name: str, _height: float, _ages: int, _harvest_season: str, _nutritional_value: int):
        super().__init__(_name, _height, _ages)
        self._harvest_season = _harvest_season
        self._nutritional_value = _nutritional_value

    def age(self) -> None:
        self._ages += 20

    def grow(self) -> None:
        self._height += 42

    def add_nut(self) -> None:
        self._nutritional_value += 20

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._ages} days old")
        print(
            f" Harvest season: {self._harvest_season}\n Nutritional value: {self._nutritional_value}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")

    print("=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red", "False")
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
    print("[make tomato grow and _age for 20 days]")
    Tomato.age()
    Tomato.grow()
    Tomato.add_nut()
    Tomato.show()


if __name__ == "__main__":
    ft_plant_types()