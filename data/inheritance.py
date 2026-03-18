class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")