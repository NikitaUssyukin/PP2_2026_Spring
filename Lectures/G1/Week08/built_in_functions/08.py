# sorted() - returns a new sorted list
# Works with any iterable, does NOT modify the original

numbers = [5, 2, 8, 1, 9, 3]

print(sorted(numbers))               # [1, 2, 3, 5, 8, 9]
print(sorted(numbers, reverse=True)) # [9, 8, 5, 3, 2, 1]
print(numbers)                       # [5, 2, 8, 1, 9, 3] - unchanged

# sorted() with key - sort by a custom criterion
words = ["banana", "apple", "cherry", "date"]

print(sorted(words))                        # alphabetical
print(sorted(words, key=len))               # by length
print(sorted(words, key=lambda w: w[-1]))   # by last character

# Sorting a list of tuples
students = [
    ("Alice", 88),
    ("Bob", 95),
    ("Charlie", 72),
    ("Diana", 91),
]

by_name = sorted(students, key=lambda s: s[0])
by_grade = sorted(students, key=lambda s: s[1], reverse=True)

print(by_name)
print(by_grade)
