class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    def bark(self):
        return "Woof!"
    
class Cat:
    def __init__(self, name, color):
        self.name = name
        self.color = color

jerry = Dog("jerry", "bulldog")
tom = Cat("tom", "black")

print(jerry.name)
print(jerry.breed)
print(tom.name)
print(tom.color)
print(jerry.bark())

