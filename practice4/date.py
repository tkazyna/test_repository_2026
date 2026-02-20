#1
# Write a Python program to subtract five days from current date
"""
from datetime import datetime, timedelta
today = datetime.now()
new_date = today - timedelta(days=5)
print("Today:", today)
print("5 days ago:", new_date)
"""
#2
# Write a Python program to print yesterday, today, tomorrow.
"""
from datetime import datetime, timedelta
today = datetime.now()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)
"""
#3
#  Write a Python program to drop microseconds from datetime.
"""
from datetime import datetime
now = datetime.now()
no_microseconds = now.replace(microsecond=0)
print(no_microseconds)
"""
#4
#  Write a Python program to calculate two date difference in seconds.
"""
from datetime import datetime
date1 = datetime(2026, 2, 20, 12, 0, 0)
date2 = datetime(2026, 2, 18, 12, 0, 0)
difference = date1 - date2
print("Seconds:", difference.total_seconds())
"""


