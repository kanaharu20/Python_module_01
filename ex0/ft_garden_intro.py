#!/usr/bin/env python3
class Plant:
    def __init__(self,_name: str,_height: float,_ages: int) -> None:
        self.name = _name
        self.height = _height
        self.ages = _ages
def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    plant1 = Plant("Rose",25,30)
    print(f"Plant: {plant1.name}")
    print(f"Height: {plant1.height,1}")
    print(f"Age: {plant1.ages}")
    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro()

