import os

relative_path = './'        # . means current working directory
absolute_path = os.getcwd() # absolute path to the current working directory

print(absolute_path)

print(os.listdir(relative_path))
print(os.listdir(absolute_path))