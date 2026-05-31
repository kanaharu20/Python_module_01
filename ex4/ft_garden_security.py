#! /usr/bin/env python3

class Plant:
    def __init__ (self,name:str,height:float,age:int) -> None:
        self._name = name
        self._height = height
        self._age = age
    def show(self) -> None:
        print(f"{self._name}: {round(self._height,1)}cm, {self._age} days old")
    def get_height(self) -> float:
        return (round(self._height,1))
    def get_age(self) -> int:
        return (self._age)
    def set_height(self,height:float) -> None:
        if height < 0:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
            return
        else:
            self._height = height
            print(f"Height updated: {self.get_height()}cm")
    def set_age(self,age:int) -> None:
        if age < 0:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
            return
        else:
            self._age = age
            print(f"Age updated: {self.get_age()} days")


def  ft_garden_security():
    print("=== Garden Security System ===")
    Rose = Plant("Rose",15.0,10);
    print(f"Plant created: ",end = "")
    Rose.show()
    print("")
    Rose.set_height(25)
    Rose.set_age(30)
    print("")
    Rose.set_height(-1)
    Rose.set_age(-1)
    print("")
    print(f"Current state: ",end = "")
    Rose.show()

if __name__ == "__main__":
    ft_garden_security()
