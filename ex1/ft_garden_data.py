#!/usr/bin/env python3

class Plant:
    def __init__ (self,_name:str,_height:float,_ages:int) -> None:
        self.name = _name
        self.height = _height
        self.ages = _ages
    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.ages} days old")

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
