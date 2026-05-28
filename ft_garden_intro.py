#!/usr/bin/env python3
class Plant:
    def __init__(self,name: str,height: int,age: int):
        self.name = name
        self.height = height
        self.age = age
def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    plant1 = Plant("Rose",25,30)
    print(f"Plant: {plant1.name}")
    print(f"Height: {plant1.height}")
    print(f"Age: {plant1.age}")
    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro()