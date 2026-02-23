# quantifiers: * + ?
# * - 0 or more repetitions
# + - 1 or more repetitions
# ? - 0 or 1 repetitions (optional)

import re

text = "ac abc abbc abbbc abbbbbbc"

# * matches 0 or more b's between a and c
print(re.findall(r"ab*c", text))     # ['ac', 'abc', 'abbc', 'abbbc', 'abbbbbbc']

# + matches 1 or more b's between a and c
print(re.findall(r"ab+c", text))     # ['abc', 'abbc', 'abbbc', 'abbbbbbc']

# ? matches 0 or 1 b between a and c
print(re.findall(r"ab?c", text))     # ['ac', 'abc']

# Practical example: matching optional "s" for plural
words = "cat cats dog dogs bird"
print(re.findall(r"\b\w+s?\b", words))
