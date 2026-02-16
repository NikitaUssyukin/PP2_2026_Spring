# Dunder (double underscore) methods are special methods Python calls automatically
# __init__ is called when creating an object
# __str__ is called by print() and str()

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

person1 = Person("Mark", 27)

print(person1)