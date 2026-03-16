file_name = 'test.txt'

file = open(file_name) # read mode is the default one

print(file)
print(type(file))

file_contents = file.read()
print(file_contents, end='')