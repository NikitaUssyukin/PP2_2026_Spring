# Classes and objects

class Person:
    name = "Mark"
    age = 27

person1 = Person()
person2 = Person()

print(person1.name)
print(person1.age)

print(person2.name)
print(person2.age)

person2.name = "Ramazan"
person2.age = 70

print(person2.name)
print(person2.age)

# Note: name and age defined directly in the class body are class attributes (shared by all instances)
# When we do person2.name = "Ramazan", we create a new instance attribute on person2,
# which shadows the class attribute. The class attribute itself is unchanged
print(Person.name)   # Still "Mark"
print(person1.name)  # Still "Mark"