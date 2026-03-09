# min() / max() with key - find extreme values by a custom criterion

words = ["cherry", "apple", "banana", "date"]

print(min(words))                  # "app-e" — alphabetically first
print(max(words))                  # "da-e" — alphabetically last

print(min(words, key=len))         # "da-e" — shortest word
print(max(words, key=len))         # "banana" or "cher-y" — first encountered longest word

print(max(sorted(words), key=len)) # "banana" - longest word that is also alphabetically first

# With a list of dicts
students = [
    {"name": "Alice", "grade": 88},
    {"name": "Bob", "grade": 95},
    {"name": "Charlie", "grade": 72},
]

best = max(students, key=lambda s: s["grade"])
worst = min(students, key=lambda s: s["grade"])

print(f"Best: {best['name']} ({best['grade']})")
print(f"Worst: {worst['name']} ({worst['grade']})")
