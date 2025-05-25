from datetime import datetime, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)

def adjust_for_weekend(birthday):
    if birthday.weekday() in (5, 6):
        return find_next_weekday(birthday, 0)
    else:
        return birthday

birthday = string_to_date("2024.03.30")
adjusted_date = adjust_for_weekend(birthday)
print(adjusted_date)

birthday = string_to_date("2024.03.29")
adjusted_date = adjust_for_weekend(birthday)
print(adjusted_date)
