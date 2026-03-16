import os

# just a name of the file - grabs the file based on the current working directory
relative_path = 'test.txt'
# absolute path to the test.txt
absolute_path = r'C:\Users\n.ussyukin\Desktop\PP2_2026_Spring\Lectures\G1\Week08\directories_and_files\test.txt'
# absolute path to the current working directory
current_path  = os.getcwd() 
print(absolute_path)

print(os.listdir(current_path))

with open(relative_path, 'r') as file:
    print("test.txt using relative_path:")
    print(file.read())

with open(absolute_path, 'r') as file:
    print("test.txt using absolute_path:")
    print(file.read())