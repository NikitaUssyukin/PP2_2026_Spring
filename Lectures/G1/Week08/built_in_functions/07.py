# zip() - combines multiple iterables element by element

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["Astana", "Almaty", "Aktau"]

# Zip two lists

print(zip(names, ages))
print(type(zip(names, ages))) # <class 'zip'>

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

print("---------")

# Zip three lists
for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, from {city}")

print("---------")

# Convert to a list of tuples
pairs = list(zip(names, ages))
print(pairs)

# If lists have different lengths, zip stops at the shortest
short = [1, 2]
long = [10, 20, 30, 40]
print(list(zip(short, long)))  # [(1, 10), (2, 20)]
