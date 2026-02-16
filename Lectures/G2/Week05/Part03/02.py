# variable scope

# https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# Global scope: variables defined at the top level are accessible everywhere,
# but to modify them inside a function you need the global keyword

counter = 0

def increment():
    global counter
    counter += 1

print(counter)  # 0
increment()
print(counter)  # 1
increment()
increment()
print(counter)  # 3

# Without the global keyword, assigning to counter inside the function
# would create a new local variable, not modify the global one
