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
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id

    def __str__(self):
        return f"Hello, {self.name}! Your ID is {self.id}"

student = Student("Achilles", 20, '25B000001')

print(student)
student.greeting()