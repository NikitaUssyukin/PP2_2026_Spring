import re

some_str = input()

pattern = r'\d'

def repl(match_obj):
    return match_obj.group(0) * 2

print(re.sub(pattern, repl, some_str))