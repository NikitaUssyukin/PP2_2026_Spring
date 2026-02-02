# Dictionaries

ourdict = {
    "ice cream": "2 dollars",
    "banana": "10 dollars",
    "pizza": "300 bucks",
    "lagman": "1000 euro"
}

ourdict["plov"] = "2000 tenge"

print(ourdict)

ourdict.update({"pizza": "5000 tenge"})

print(ourdict)

del ourdict["pizza"] # KeyError if key is not present

print(ourdict)
