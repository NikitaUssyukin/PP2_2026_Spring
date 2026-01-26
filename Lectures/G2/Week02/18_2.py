# Strings

# strings are immutable in python - you cannot change the string directly

a = "cat"

a = a.replace('c', 'r')
print(a)

# or

a = "cat"
b = 'c'
c = 'r'

a = a.replace(b, c)
print(a)