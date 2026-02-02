# Functions

x = 1 # global variable

def func():
    global x # allows to modify x as a local variable within a function
    x += 1
    print(x)

func()
print(x)