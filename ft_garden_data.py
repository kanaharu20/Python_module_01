#!/usr/bin/env python3
class Plant:
    def __init__ (self,name:str,height:float,age:int):
        self.name = name
        self.height = height
        self.age = age
    def show(self) -> None:
        print(f"{self.name}: {round(self.height)}cm, {self.age} days old")

def ft_garden_data() -> None:
    print("=== Garden Plant Registry ===")
    Rose = Plant("Rose",25,30)
    Sunflower = Plant("Sunflower",80,45)
    Cactus = Plant("Cactus",15,120)
    Plant.show(Rose)
    Plant.show(Sunflower)
    Plant.show(Cactus)

if __name__ == "__main__" :
    ft_garden_data()
