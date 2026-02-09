# The 'is' keyword - identity vs equality
# == checks if two values are equal
# is checks if two variables point to the exact same object in memory

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True  - same values
print(a is b)  # False - different objects in memory

print(a == c)  # True  - same values
print(a is c)  # True  - same object

# id() shows the memory address of an object
print(id(a))
print(id(b))   # different from id(a)
print(id(c))   # same as id(a)

# Most common use - checking for None
x = None
print(x is None)   # True  - preferred way
print(x == None)   # True  - works, but 'is None' is the convention

# With class instances:

class Person:
    def __init__(self, name):
        self.name = name
    
    # Example of a custom __eq__
    # def __eq__(self, other):
    #     return self.name == other.name

p1 = Person("Alice")
p2 = Person("Alice")
p3 = p1

print(p1 == p2)  # False - different objects (no custom __eq__ defined)
print(p1 is p2)  # False - different objects
print(p1 is p3)  # True  - same object

print(id(p1))
print(id(p2))
print(id(p3))
