#!/usr/bin/env python3

class Plant:
    def __init__ (self,name:str,height:float,age:int) -> None:
        self.name = name
        self.height = height
        self.age = age
    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.age} days old")
    def grow(self) -> None:
        plant.height += 0.4
    def age(self) -> None:
        plant.age += 1
Rose = Plant("Rose",25.0,30)
Oak = Plant("Oak",200.0,365)
Cactus = Plant("Cactus",5.0,90)
Sunflower = Plant("Sunflower",80.0,45)
Fern = Plant("Fern",15.0,120)

def ft_plant_factory() ->None:
    Rose.show()
    Oak.show()
    Cactus.show()
    Sunflower.show()
    Fern.show()

if __name__ == "__main__":
    ft_plant_factory()