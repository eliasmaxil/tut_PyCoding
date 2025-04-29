"""
File: mytutorial.py
Author: Jorge Elias
Description: This script demonstrates object-oriented programming concepts in Python.
"""

class Animal:
    """ Flexible class to instantiate diverse features"""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
            
    def __str__(self):
        """List the name and type of each attribute"""
        attributes = [f"{key}: {type(value).__name__}" for key, value in self.__dict__.items()]
        attributes_str = ", ".join(attributes)
        return f"Animal with attributes:\n{attributes_str}"

    @classmethod
    def class_method(cls):
        """Class method"""
        return "This is a class method!"
    
    @staticmethod
    def static_method():
        """Static method"""
        return "This is a static method!"
    

class Cat(Animal):
    """Class to represent a Cat"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        for key, value in kwargs.items():
            setattr(self, key, value)
        
    
    def __str__(self):
        """List the name and type of each attribute"""
        attributes = [f"{key}: {type(value).__name__}" for key, value in self.__dict__.items()]
        attributes_str = ", ".join(attributes)
        return f"Cat with attributes:\n{attributes_str}"
    

if __name__ == "__main__":

    animal = Animal(name="Dog", age=5, color="Brown")
    print(animal)
    print(Animal.class_method())
    print(Animal.static_method())

    bicha = Cat(name="Bicha", age=13, colors=["Golden", "Black", "White"], weiwght=5, height=10)
    print(bicha)
    print(bicha.colors)