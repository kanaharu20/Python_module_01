#!/usr/bin/env python3
from ft_garden_data import Plant

def grow(plant) -> None:
    plant.height += 0.4

def age(plant) -> None:
    plant.age += 1

def ft_plant_growth() -> None:
    print("=== Garden Plant Growth ===")
    Rose = Plant("Rose",25,30)
    for i in range(7):
        print(f"=== Day {i} ===")
        grow(Rose)
        age(Rose)
        Plant.show(Rose)
    print(f"Growth this week: {round(Rose.height - 25.0)}cm")

if __name__ == "__main__":
    ft_plant_growth()
