import time
import os

file_name = 'new.txt'

with open(file_name, 'w') as file:
    file.write('Last words before removal...')
    # in 'x' mode, if file does not exist, it is created
    # otherwise - FileExistsError: [Errno 17] File exists: 'new.txt'

time.sleep(3) # 3-second delay

os.remove(file_name)

'''
'r'  -  read mode
'w'  -  write mode
'a'  -  append mode
'x'  -  create mode
'''
