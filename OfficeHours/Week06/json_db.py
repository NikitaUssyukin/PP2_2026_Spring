import json

data = dict()

def retreive_data():
    global data
    json_file = 'data.json'
    try:
        with open(json_file, 'r') as file:
            data = json.load(file)
    except:
        print("Something is wrong with data.json! Initializing with empty data...")

def save_data():
    global data
    json_file = 'data.json'
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

def add_value():
    global data
    input_data = input().split()
    if len(input_data) != 2:
        print("invalid number of arguments: must be exactly 2, key and value")
        return
    key, value = input_data
    if value.isdecimal():
        value = int(value)
    data[key] = value

def del_key():
    global data
    input_data = input().split()
    if len(input_data) != 1:
        print("invalid number of arguments: must be exactly 1 - key to delete")
        return
    key = input_data[0]
    if data.get(key) is None:
        print("the key does not exist in data - skipping")
        return
    del data[key]

def read_from_json_file():
    global data
    input_data = input().split()
    if len(input_data) != 1:
        print("invalid number of arguments: must be exactly 1 - name of the json file")
        return
    json_file = input_data[0]
    with open(json_file, 'r') as file:
        data = json.load(file)

def save_to_json_file():
    global data
    input_data = input().split()
    if len(input_data) != 1:
        print("invalid number of arguments: must be exactly 1 - name of the json file")
        return
    json_file = input_data[0]
    with open(json_file, 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == '__main__':

    retreive_data()

    while True:
        command = input("Enter command: ")
        if command == "exit":
            break
        elif command == "add_value":
            add_value()
        elif command == "del_key":
            del_key()
        elif command == "read_from_json_file":
            read_from_json_file()
        elif command == "save_to_json_file":
            save_to_json_file()
        elif command == "print_data":
            print(data)
        else:
            print("invalid command!")

    save_data()

