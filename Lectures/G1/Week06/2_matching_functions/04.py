import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = '[Jj]ohn' # our regex

results = re.finditer(pattern, text_to_match)

print(results) # iterator with match objects

for result in lst:
    print(result)

# making a list of match objects from an iterator
lst = list(results)

print(lst)