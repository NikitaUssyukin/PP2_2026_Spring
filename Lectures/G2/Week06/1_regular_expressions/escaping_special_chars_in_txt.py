# extra example shown on the lecture - not mandatory

with open('../test.txt', 'r') as file:
    res = file.read()
    special_chars = "\"\'$#"
    for x in special_chars:
        res = res.replace(x, "\\" + x)
    print(res)