import os

name = r'C:\Users\n.ussyukin\Desktop\PP2_2026_Spring\Lectures\G1\Week08\directories_and_files\11.py'

print(os.access(name, os.F_OK)) # Existence
print(os.access(name, os.R_OK)) # Readability
print(os.access(name, os.W_OK)) # Writeability
print(os.access(name, os.X_OK)) # Executeability
