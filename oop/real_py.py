"""
File: real_py.py
Author: Jorge
Date: 2025-04-23
Description: Tutorial de OOP. 
URL: https://realpython.com/python3-object-oriented-programming/
"""

class DomesticAnimal:
    pet = True
    lives_in_house = True
    def __init__(self):
        self.colors = ["brown"]
        self.legs = 4
        self.mammal = True

class Dog(DomesticAnimal):
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        super().__init__()
        self.colors.append("black")
        
    
    # Class method
    @classmethod
    def bark(cls):
        return "Bark!"
    
    # Static method
    @staticmethod
    def get_action():
        return "Move tail (static method)!"

    # Instance method
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound} (Dog class)!"
        

# Child classes from Dog
class Bulldog(Dog):
    pass

class Poodle(Dog):
    # Specific speak method for Poodle
    def speak(self, sound):
        return f"Poodles like {self.name} bark {sound} with a twist!" 

class Bobtail(Dog):
    def speak(self, sound="Arf"):
        return super().speak(sound) + f" .(Bobtail class)!"



if __name__ == "__main__":
    
    # buddy = Dog("Buddy", 9)
    # print(f"buddy: {buddy}")
    
    miles = Dog("Miles", 4)
    
    print(f"miles: {miles}")
    print(f".colors[]: {miles.colors}")
    print(f".bark(): {miles.bark()}. @classmethod")
    print(f".speak(-): {miles.speak(sound='Woof!')}")
    print(f".speak(-): {miles.speak(sound='Hoooooola!!')}")
    print(f"miles.__dict__: {miles.__dict__}")
    print()
    
    # Child classes
    tiny = Poodle("Tiny", 15)
    camila = Bobtail("Camila", 2)
        
    print(f"tiny: {tiny}")
    print(f"camila: {camila}")
    print(f"Camila.speak(-): {camila.speak(sound='Guau!')}")
    print(f"Tiny.speak(-): {tiny.speak(sound='Woof...')}")
    print(f"Tiny.get_action(): {tiny.get_action()}")
    