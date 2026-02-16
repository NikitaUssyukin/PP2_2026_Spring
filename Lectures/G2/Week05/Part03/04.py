# variable scope

# Summary: LEGB rule — Python looks up variable names in this order:
# L - Local (inside the current function)
# E - Enclosing (in the outer function, for nested functions)
# G - Global (at the module/file level)
# B - Built-in (Python's built-in names like print, len, etc.)

x = "global"

def outer():
    x = "enclosing"

    def inner():
        x = "local"
        print(f"inner sees: {x}")     # local

    inner()
    print(f"outer sees: {x}")         # enclosing

outer()
print(f"module level sees: {x}")      # global
