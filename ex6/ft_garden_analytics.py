#! usr/bin/env python3

class Plant:
    class Data:
        def __init__(self,_cnt_show:int,_cnt_grow:int,_cnt_age:int):
            self._cnt_show = _cnt_show
            self._cnt_grow = _cnt_grow
            self._cnt_age = _cnt_age

    def __init__(self, _name: str, _height: float, _age: int) -> None:
        self._name = _name
        self._height = _height
        self._age = _age
        self.data = Data(0,0,0)

    def anonymous(self):
        Unknown_plant = Plant("Unknown_plant",0.0,0)

def check_year(age:int):
    if age > 365:
        print(f"Is {age} days more than a year? -> True")
    else:
        print(f"Is {age} days more than a year? -> False")

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
        self.Data._cnt_show += 1

class Seed(Flower):
    def __init__(self, _name: str, _height: float, _age: int, _color: str, _status: bool,__num_seeds:int):
        super().__init__(self, _name: str, _height: float, _age: int, _color: str, _status: bool)
        self._num_seeds = _num_seeds

    def bloom(self) -> None:
        self._status = True
        self._num_seeds = 42

    def show(self):
        print(f"{self.name}: cm, {self.age} days old\n"
        f" Color: {self.color}\n
        f" {self.name} has not bloomed yet\n"
        f" Seeds: {self._num_seeds}")
        self.Data._cnt_show += 1

class Tree(Plant):
    def __init__(self, _name: str, _height: float, _age: int, _trunk_diameter: float):
        self._trunk_diameter = _trunk_diameter
        super().__init__(_name, _height, _age)

    class Data(Plant.data)
        def __init__(self,_cnt_show:int,_cnt_grow:int,_cnt_age:int,_cnt_shade:int)
        self._cnt_shade = _cnt_shade
        super().__init__(_cnt_show:int,_cnt_grow:int,_cnt_age:int)

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm, {self._age} days old\n Trunk diameter: {self._trunk_diameter}cm")
        self.Data._cnt_show += 1

    def produce_shade(self) -> None:
        print("[asking the oak to produce shade]")
        print("Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.")
        self.Data._cnt_shade += 1

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

def statistics(Plant:Plant):


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