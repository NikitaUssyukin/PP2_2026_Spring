# any() - returns True if at least one element is truthy
# all() - returns True if all elements are truthy

numbers = [0, 0, 0, 1]
print(any(numbers))  # True - at least one non-zero
print(all(numbers))  # False - not all are non-zero

numbers = [1, 2, 3]
print(any(numbers))  # True
print(all(numbers))  # True

numbers = [0, 0, 0]
print(any(numbers))  # False
print(all(numbers))  # False

# Practical use: check conditions across a collection
ages = [18, 21, 16, 25, 14]

all_adults = all(age >= 18 for age in ages)
any_adults = any(age >= 18 for age in ages)

print(f"All adults: {all_adults}")   # False
print(f"Any adults: {any_adults}")   # True
