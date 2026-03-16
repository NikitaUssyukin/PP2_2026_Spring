file_name = 'test.txt'

file = open(file_name, 'w')

'''
'r'  -  read mode
'w'  -  write mode
'a'  -  append mode
'x'  -  create mode
'''

print(file)
print(file.read(), end='') # Error - file open in write mode
                           # In write mode, you cannot read a file