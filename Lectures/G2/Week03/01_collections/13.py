# Combining collections, on the example of dictionary of dictionaries

ourdict = { 
    "otherDict": {
        "key": "value"
    }
}

ourdict["otherDict"]["key"] = "new value"

print(ourdict)
print(ourdict["otherDict"])