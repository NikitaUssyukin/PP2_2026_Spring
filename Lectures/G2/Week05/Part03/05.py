# dates

# https://docs.python.org/3/library/datetime.html

from datetime import datetime, date, time

# Current date and time
now = datetime.now()
print(now)

# Accessing individual components
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

# Date only and time only
today = date.today()
print(today)

current_time = now.time()
print(current_time)
