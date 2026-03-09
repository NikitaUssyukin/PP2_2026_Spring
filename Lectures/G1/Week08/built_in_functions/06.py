# enumerate() - adds an index to each element during iteration

fruits = ["apple", "banana", "cherry", "mango"]

# Without enumerate:
for i in range(len(fruits)):
    print(i, fruits[i])

print("---------")

# With enumerate:
for i, fruit in enumerate(fruits):
    print(i, fruit)

print("---------")

# Custom start index
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
