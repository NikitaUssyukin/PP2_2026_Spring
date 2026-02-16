# dates

# https://docs.python.org/3/library/datetime.html#timedelta-objects

from datetime import datetime, timedelta

now = datetime.now()

# timedelta represents a duration — the difference between two dates/times
one_week = timedelta(weeks=1)
two_days = timedelta(days=2)
three_hours = timedelta(hours=3)

print(now + one_week)       # one week from now
print(now - two_days)       # two days ago
print(now + three_hours)    # three hours from now

# Difference between two dates
new_year = datetime(2027, 1, 1)
until_new_year = new_year - now

print(f"Days until 2027: {until_new_year.days}")
print(f"Total seconds: {until_new_year.total_seconds()}")
