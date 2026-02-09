# Inheritance

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"
    
    def greeting(self):
        print(f"Hello, {self.name}!")

class Student(Person):
    pass

student = Student("Achilles", 20)

print(student)
student.greeting()