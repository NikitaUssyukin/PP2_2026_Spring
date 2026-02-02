# Combining collections, on the example of dictionary of dictionaries

ourdict = { 
    "key1": 1,
    "key2": -5,
    "key3": 100
}

max_key = None
max_value = None

for k, v in ourdict.items():
    if max_key is None and max_value is None:
        max_key = k
        max_value = v
    elif v > max_value:
            max_key = k
            max_value = v

if max_key is None and max_value is None:
    print("dict is empty")
else:
    print(max_key, max_value)