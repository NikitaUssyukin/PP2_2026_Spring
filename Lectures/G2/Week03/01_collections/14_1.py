# Combining collections, on the example of dictionary of dictionaries

ourdict = { 
    "key1": 1,
    "key2": -5,
    "key3": 100
}

# print(list(ourdict.items()))

# for item in list(ourdict.items()):
#     print(item)

max_key, max_value = max(list(ourdict.items()), key=lambda items : items[1])

print(max_key, max_value)