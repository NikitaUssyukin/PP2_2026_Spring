# Classes and objects

class Person:
    def __init__(self):       # special "dunder" method, creates a new instance of the class
        print("init called!") # it is called every time we create a new instance
    name = "Mark"
    age = 27

person1 = Person()
person2 = Person()