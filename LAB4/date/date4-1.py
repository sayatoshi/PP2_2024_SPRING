from datetime import datetime, timedelta

current_date = datetime.now().date()

result_date = current_date - timedelta(days=5)

print("Current Date:", current_date)
print("Date five days ago:", result_date)


