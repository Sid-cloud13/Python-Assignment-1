# OOPS Concept

class Dog:
    #class attribute ( Shared by all instances)
    species = "Canis familiaris"

    # Contructor (initializer)
    def __init__(self, name, age):
        # Instance attributes (unique to each instance)
        self.name = name
        self.age = age
        self.__age = age

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"
    
    # Another instance method
    def get_age(self):
        return f"{self.name} is 47 years old."
    
    # Creating instances (objects) of the dog class
dog1 = Dog("buddy", 3)
dog2 = Dog("charlie", 5)

    # Accessing attributes and methods


print(dog1.bark())
print(dog2.get_age())
print(dog1.species)
