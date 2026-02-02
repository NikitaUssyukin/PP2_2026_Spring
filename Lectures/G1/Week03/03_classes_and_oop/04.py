# Classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Mark", 27)

print(person1.name)
print(person1.age)