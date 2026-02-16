# variable scope

# https://docs.python.org/3/tutorial/classes.html#python-scopes-and-namespaces

# Local scope: variables defined inside a function are local to that function

def greet():
    message = "Hello!"  # local variable
    print(message)

greet()

# print(message)  # NameError: 'message' is not defined outside the function
