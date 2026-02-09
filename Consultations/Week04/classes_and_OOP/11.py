# Value types vs Reference types
# In Python, everything is an object. But some types are immutable (behave like "values")
# and some are mutable (behave like "references")

# Immutable types: int, float, str, bool, tuple
# Reassigning creates a new object - the original is unaffected

a = 10
b = a
b = 20

print(type(a)) # <class 'int'>
print(type(b)) # <class 'int'>

print(a)  # 10 - unchanged
print(b)  # 20

name1 = "Alice"
name2 = name1
name2 = "Bob"

print(name1)  # "Alice" - unchanged
print(name2)  # "Bob"

# Mutable types: list, dict, set, and class instances
# Assignment copies the reference, not the data - both variables point to the same object

list1 = [1, 2, 3]
list2 = list1       # list2 points to the SAME list
list2.append(4)

print(list1)  # [1, 2, 3, 4] - both affected!
print(list2)  # [1, 2, 3, 4]

# Same applies to class instances

class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
p2 = p1              # p2 points to the SAME object
p2.name = "Bob"

print(p1.name)  # "Bob" - both affected!
print(p2.name)  # "Bob"
