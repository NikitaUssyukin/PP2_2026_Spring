import json

source_json = input()
patch_json = input()

source = json.loads(source_json)
patch = json.loads(patch_json)

# Checking if the input is correct
# print(source)
# print(patch)

# Checking the .items() method
# print(patch.items())

def apply_patch(source, patch):
    for key, value in patch.items():
        if source.get(key) is None and value is not None:
            source[key] = value
        elif source.get(key) is not None and value is None:
            del source[key]
        elif value is not None:
            if isinstance(value, dict) and isinstance(source.get(key), dict):
                source[key] = apply_patch(source[key], value)
            else:
                source[key] = value
    return source

patched_source = apply_patch(source, patch)
patched_source_json = json.dumps(patched_source, separators=(',', ':'), sort_keys=True)

# Demonstration that the output of .dumps() method is just a string (class str)
# print(type(patched_source_json))
# print(type('hello'))

print(patched_source_json)