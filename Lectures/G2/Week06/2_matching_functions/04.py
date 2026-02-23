import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net."

pattern = '[Jj]ohn' # our regex

results = re.finditer(pattern, text_to_match)

print(results) # iterator with match objects

# making a list of match objects from an iterator
lst = list(results)
print(lst)

# or iterating directly over the elements of the iterator
for result in results:
    print(result)
