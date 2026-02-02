# Lambda functions

# A lambda is a small anonymous function
# Syntax: lambda arguments: expression

# Regular function
def add(a, b):
    return a + b

print(add(3, 5))

# Equivalent lambda
add_lambda = lambda a, b: a + b

print(add_lambda(3, 5))

# Lambdas are often used with functions like map, filter, sorted

numbers = [1, 2, 3, 4, 5]

# Using lambda with map
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Using lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Using lambda with sorted
cars = [("BMW", 1995), ("Toyota", 2020), ("Mercedes", 2015)]
sorted_by_year = sorted(cars, key=lambda car: car[1])
print(sorted_by_year)
