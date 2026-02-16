# dates

# https://docs.python.org/3/library/datetime.html#strftime-strptime-behavior

from datetime import datetime

# Creating a specific date
new_year = datetime(2026, 1, 1, 0, 0, 0)
print(new_year)

# Formatting: datetime → string (strftime = "string format time")
now = datetime.now()
print(now.strftime("%Y-%m-%d"))         # 2026-02-09
print(now.strftime("%d/%m/%Y"))         # 09/02/2026
print(now.strftime("%H:%M:%S"))         # 14:30:00
print(now.strftime("%A, %B %d, %Y"))   # Monday, February 09, 2026

# Parsing: string → datetime (strptime = "string parse time")
date_string = "25-12-2026"
parsed = datetime.strptime(date_string, "%d-%m-%Y")
print(parsed)
print(type(parsed))
