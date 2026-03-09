import os

path = os.getcwd()
# get cwd - current working directory

entries = os.scandir(path)

print(entries)
print(type(entries))

for entry in entries:
    if entry.name == '01.py':
        print('Name:', entry.name)
        print('Full path (including the file):', entry.path)
        print('Full path (excluding the file):', entry.path[:-len(entry.name)])
        print('-----------------')