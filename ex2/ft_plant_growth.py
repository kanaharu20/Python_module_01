#!/usr/bin/env python3

class Plant:
    def __init__ (self,name:str,height:float,age:int) -> None:
        self.name = name
        self.height = height
        self.age = age
    def show(self) -> None:
        print(f"{self.name}: {round(self.height,1)}cm, {self.age} days old")
    def grow(self) -> None:
        self.height += 0.4
    def age(self) -> None:
        self.age += 1

def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    Rose = Plant("Rose",25.0,30)
    Rose.show()
    for i in range(7):
        print(f"=== Day {i} ===")
        Rose.grow()
        Rose.age()
        Rose.show()
    print(f"Growth this week: {round(Rose.height - 25,1)}cm")

if __name__ == "__main__":
    ft_plant_growth()
