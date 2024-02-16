from datetime import datetime

# Get the current date and time
a = datetime.now()

# Drop microseconds
a_b = a.replace(microsecond=0)

# Print the result
print("Current datetime without microseconds:", a_b)
