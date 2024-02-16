from datetime import datetime

date_str1 = input("Enter the first date: ")
date_str2 = input("Enter the second date: ")

date1 = datetime.strptime(date_str1, "%Y-%m-%d %H:%M")
date2 = datetime.strptime(date_str2, "%Y-%m-%d %H:%M")

time_diff = date2 - date1

days = time_diff.days
hours = time_diff.seconds // 3600
minutes = (time_diff.seconds // 60) % 60

print(f"Difference: {days} days, {hours} hours, {minutes} minutes")
