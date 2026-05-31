#! usr/bin/env python3

class Plant:
    def __init__(self, _name: str, _height: float, _age: int) -> None:
        self._name = _name
        self._height = _height
        self._age = _age
    def check_year(age:int):
        if age > 365:
            print(f"Is {age} days more than a year? -> True")
        else:
            print(f"Is {age} days more than a year? -> False")
    def anonymous():
        Unknown plant = Plant("Unknown plant",0.0,0)


class Flower(Plant):
    def __init__(self, _name: str, _height: float, _age: int, _color: str, _status: bool):
        super().__init__(_name, _height, _age)
        self._color = _color
        self._status = _status

    def show(self) -> None:
        if self._status == True:
            print(
                f"{self._name}: {round(self._height, 1)}cm, {self._age} days old\n _color: {self._color}")
            print(f" {self._name} is blooming beautifully!")
        else:
            print("[asking the rose to bloom]")

    def bloom(self) -> None:
        self._status = True

class Seed(Flower):
    def __init__(self, _name: str, _height: float, _age: int, _color: str, _status: bool,__num_seeds:int):
        super().__init__(self, _name: str, _height: float, _age: int, _color: str, _status: bool)
        self._num_seeds = _num_seeds
    def 


class Tree(Plant):
    def __init__(self, _name: str, _height: float, _age: int, _trunk_diameter: float):
        super().__init__(_name, _height, _age)
        self._trunk_diameter = _trunk_diameter

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old\n Trunk diameter: {self._trunk_diameter}cm")

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")


class Vegetable(Plant):
    def __init__(self, _name: str, _height: float, _age: int, _harvest_season: str, _nutritional_value: int):
        super().__init__(_name, _height, _age)
        self._harvest_season = _harvest_season
        self._nutritional_value = _nutritional_value

    def age(self) -> None:
        self._age += 20

    def grow(self) -> None:
        self._height += 42

    def add_nut(self) -> None:
        self._nutritional_value += 20

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old")
        print(f" Harvest season: {self._harvest_season}\n Nutritional value: {self._nutritional_value}")

def statics(self):

def ft_garden_analytics():
    print("=== Garden statistics ===")
    print("=== Check year-old")
    check_year(30)
    check_year(400)

    print("\n=== Flower")
    Rose = Flower("Rose",15.0,10,red,False)
    Rose.show()
    static("Rose")
    Rose.bloom()
    Rose.grow()
    Rose.show()
    static("Rose")

    print("\n=== Tree")
    Oak = Tree("Oak",200.0,365,5.0)
    statics("Oak")
    Oak.produce_shade()
    statics("Oak")

    print("\n=== Seed")
    Sunflower = Seed("Sunflower",80.0,45,"yellow",False,0)
    Sunflower.bloom()
    Sunflower.show()
    Sunflower.grow()
    Sunflower.age()
    statics("Sunflower")

    print("\n=== Anonymous")
if __name__ == "__main__"
    ft_garden_analytics()