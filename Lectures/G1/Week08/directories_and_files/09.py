import os

def check_dir_file(name):
    return 'Is file/Is folder: ' + str(os.path.isfile(name)) + '/' + str(os.path.isdir(name))

path = os.getcwd()

for entry in os.listdir(path):
    full_path = os.path.join(path, entry)
    existence = os.access(full_path, os.F_OK)
    readability = os.access(full_path, os.R_OK)
    writability = os.access(full_path, os.W_OK)
    executability = os.access(full_path, os.X_OK)
    if not existence:
        print(check_dir_file(full_path))
        print(entry, 'does not exist')
        break
    if not readability:
        print(check_dir_file(full_path))
        print(entry, 'no access to read')
        break
    if not writability:
        print(check_dir_file(full_path))
        print(entry, 'no access to write')
        break
    if not executability:
        print(check_dir_file(full_path))
        print(entry, 'no access to execute')
        break
