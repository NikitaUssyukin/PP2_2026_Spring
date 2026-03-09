# https://docs.python.org/3/library/functions.html

lst = [1, 2, 3]

map_result = map(lambda x: 2*x, lst)

print(type(map_result)) # <class 'map'>
print(list(map_result)) # [2, 4, 6]

for num in map(lambda x: 2*x, lst):
    print(num)