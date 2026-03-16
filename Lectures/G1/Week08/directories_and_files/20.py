import time
import os

file_name = 'new.txt'

with open(file_name, 'w') as file:
    file.write('Last words before removal...') 

time.sleep(3) # 3-second delay

os.remove(file_name)
