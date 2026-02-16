# Method overriding - any method can be overridden in a subclass

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} says: Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says: Meow!")

animal = Animal("Generic animal")
dog = Dog("Rex")
cat = Cat("Whiskers")

animal.speak()
dog.speak()
cat.speak()
