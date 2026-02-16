# variable scope

# https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# Nonlocal scope: used in nested functions to modify a variable
# from the enclosing (outer) function's scope.

def outer():
    count = 0

    def inner():
        nonlocal count
        count += 1
        print(f"inner: count = {count}")

    inner()
    inner()
    inner()
    print(f"outer: count = {count}")

outer()

# Without nonlocal, assigning to count in inner() would create
# a new local variable inside inner, leaving outer's count unchanged.
