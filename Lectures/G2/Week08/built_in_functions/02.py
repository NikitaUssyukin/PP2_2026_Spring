# https://docs.python.org/3/library/functions.html

lst = [1, 2, 3]

def func(x): # using this function function instead of lambda
    return 2*x

map_result = map(func, lst)

print(type(map_result)) # <class 'map'>
lst = list(map_result)  
print(lst)              # [2, 4, 6]

for num in lst:
    print(num)