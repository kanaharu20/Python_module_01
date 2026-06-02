#!/usr/bin/env python3
class Plant:
    def __init__(self, name: str, height: float, ages: int) -> None:
        self._name = name
        self._height = height
        self._ages = ages


def ft_garden_intro() -> None:
    print("=== Welcome to My Garden ===")
    Rose = Plant("Rose", 25, 30)
    print(f"Plant: {Rose._name}")
    print(f"Height: {Rose._height}cm")
    print(f"Age: {Rose._ages} days")
    print("\n=== End of Program ===")


if __name__ == "__main__":
    ft_garden_intro()
