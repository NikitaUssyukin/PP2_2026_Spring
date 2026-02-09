# Classes and objects

class Person:
    def __init__(self, name, age): # self points to the current instance of the class that is being created
        self.name = name # class instance (object) attributes
        self.age = age

person1 = Person("Mark", 27)
person2 = Person("Dima", 34)

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)

# What we cannot do:
# print(Person.name)
# print(Person.age)
# In this example, class Person has no class attributes
# so trying to access them results in an error