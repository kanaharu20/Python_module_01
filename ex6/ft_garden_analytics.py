#! /usr/bin/env python3

class Plant:
    def __init__(self, _name: str, _height: float, _ages: int) -> None:
        self._name = _name
        self._height = _height
        self._ages = _ages
        self._data: Plant.Data = Plant.Data()

    class Data:
        def __init__(self) -> None:
            self._cnt_show: int = 0
            self._cnt_grow: int = 0
            self._cnt_age: int = 0

        def incl_grow(self) -> None:
            self._cnt_grow += 1

        def incl_age(self) -> None:
            self._cnt_age += 1

        def incl_show(self) -> None:
            self._cnt_show += 1

        def show(self) -> None:
            print(f"Stats: {self._cnt_grow} grow, "
                  f"{self._cnt_age} age, "
                  f"{self._cnt_show} show")

    def age(self) -> None:
        self._ages += 1
        self._data.incl_age()

    def grow(self) -> None:
        self._height += 8.0
        self._data.incl_grow()

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height, 1)}cm, "
            f"{self._ages} days old"
            )
        self._data.incl_show()

    def get_name(self) -> str:
        return self._name

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown_plant", 0.0, 0)

    @staticmethod
    def check_year(age: int):
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")


class Flower(Plant):
    def __init__(
        self,
        _name: str,
        _height: float,
        _ages: int,
        _color: str,
        _status: bool
    ):
        super().__init__(_name, _height, _ages)
        self._color = _color
        self._status = _status

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height,1)}cm, "
            f"{self._ages} days old"
            )
        print(f" Color: {self._color}")
        if self._status:
            print(
                f" {self._name} is "
                "blooming beautifully!"
                )
        else:
            print(" Rose has not bloomed yet")
        self._data.incl_show()

    def bloom(self) -> None:
        print("[asking the rose to bloom]")
        self._status = True


class Seed(Flower):
    def __init__(
        self,
        _name: str,
        _height: float,
        _ages: int,
        _color: str,
        _status: bool,
        _num_seeds: int
    ) -> None:
        super().__init__(_name, _height, _ages, _color, _status)
        self._num_seeds = _num_seeds

    def bloom(self) -> None:
        self._status = True
        self._num_seeds = 42

    def show(self) -> None:
        print(
            f"{self._name}: {round(self._height,1)}cm,"
            f" {self._ages} days old"
        )
        print(f" Color: {self._color}")
        print(f" {self._name} has not bloomed yet")
        print(f" Seeds: {self._num_seeds}")
        self._data.incl_show()


class Tree(Plant):
    class Tree_Data(Plant.Data):
        def __init__(self) -> None:
            super().__init__()
            self._cnt_shade: int = 0

        def incl_shade(self) -> None:
            self._cnt_shade += 1

        def show(self) -> None:
            super().show()
            print(f" {self._cnt_shade} shade")

    def __init__(
        self,
        _name: str,
        _height: float,
        _ages: int,
        _trunk_diameter: float
    ):
        super().__init__(_name, _height, _ages)
        self._trunk_diameter = _trunk_diameter
        self._data = Tree.Tree_Data()

    def show(self) -> None:
        print(f"{self._name}: {round(self._height,1)}cm, "
              f"{self._ages} days old\n "
              f"Trunk diameter: {self._trunk_diameter}cm")
        self._data.incl_show()

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")
        self._data.incl_shade()


def show_statistics(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant._data.show()


def ft_garden_analytics():
    print("=== Garden statistics ===")

    print("=== Check year-old")
    Plant.check_year(30)
    Plant.check_year(400)

    print("\n=== Flower")
    Rose = Flower("Rose", 15.0, 10, "red", False)
    Rose.show()
    show_statistics(Rose)
    Rose.bloom()
    Rose.grow()
    Rose.show()
    show_statistics(Rose)

    print("\n=== Tree")
    Oak = Tree("Oak", 200.0, 365, 5.0)
    Oak.show()
    show_statistics(Oak)
    Oak.produce_shade()
    show_statistics(Oak)

    print("\n=== Seed")
    Sunflower = Seed("Sunflower", 80.0, 45, "yellow", False, 0)
    Sunflower.show()
    print(f"[make {Sunflower.get_name()} grow, age and bloom]")
    Sunflower.grow()
    Sunflower.age()
    Sunflower.bloom()
    Sunflower.show()
    show_statistics(Sunflower)

    print("\n=== Anonymous")
    Unknown_plant = Plant.anonymous()
    Unknown_plant.show()
    show_statistics(Unknown_plant)


if __name__ == "__main__":
    ft_garden_analytics()
