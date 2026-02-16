# json

# https://docs.python.org/3/library/json.html#module-json

# Serialization: Python object → JSON string

import json

ferrari = {
    "make": "Ferrari",
    "model": "458 Italia",
    "price": 300000,
    "features": ["V8", "rear-wheel drive", "carbon ceramic brakes"],
    "available": True
}

json_string = json.dumps(ferrari)

print(type(json_string))
print(json_string)

# indent for pretty-printing
json_pretty = json.dumps(ferrari, indent=4)
print(json_pretty)
