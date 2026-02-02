# Dictionaries

ourdict = {
    "ice cream": "2 dollars",
    "banana": "10 dollars",
    "pizza": "300 bucks",
    "lagman": "1000 euro"
}

for key in ourdict:                  # iterate over keys of the dictionary
    print(key, ourdict[key])

for value in ourdict.values():       # iterate over values of the dictionary
    print(value)

for key, value in ourdict.items():   # iterate over items (key, value) of the dictionary
    print(key, value)
