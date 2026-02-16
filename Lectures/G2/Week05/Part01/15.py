# iterators and generators

# generator expressions

# https://docs.python.org/3/tutorial/classes.html#generator-expressions

start = int(input())
stop = int(input())
step = int(input())

gen_exp = (i**3 for i in range(start, stop, step))

for num in gen_exp: # generator expression in parenthesis
    print(num)