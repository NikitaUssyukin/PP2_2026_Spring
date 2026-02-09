# OOP - Object-Oriented Programming
# A way to structure code around "objects" - entities that combine data and behavior.
# A class is a blueprint (like a custom data type)
# An object is an instance of that blueprint (like a variable of that data type)

class Person:
    name = "Mark" # class attributes
    age = 27

person = Person()

print(type(person))

print(person.name) # accessing the class attribute via the person object
print(person.age)

print(Person.name) # accessing the class attribute directly via the class itself