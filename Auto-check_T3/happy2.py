from datetime import timedelta, datetime

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday=0):
    days_ahead = (weekday - start_date.weekday() + 7) % 7
    if days_ahead == 0:
        days_ahead = 7
    return start_date + timedelta(days=days_ahead)

start_date = string_to_date("2024.12.12")
next_monday = find_next_weekday(start_date, 0) 
print(next_monday)
next_friday = find_next_weekday(start_date, 4)
print(next_friday)