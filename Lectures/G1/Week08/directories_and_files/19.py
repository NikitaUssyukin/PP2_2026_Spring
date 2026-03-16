file_name = 'new.txt'

with open(file_name, 'x') as file:
    pass
    # in 'x' mode, if file does not exist, it is created
    # otherwise - FileExistsError: [Errno 17] File exists: 'new.txt'

'''
'r'  -  read mode
'w'  -  write mode
'a'  -  append mode
'x'  -  create mode
'''
