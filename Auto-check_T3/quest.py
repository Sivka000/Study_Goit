from datetime import datetime, date, timedelta

def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()

def date_to_string(date):
    return date.strftime("%Y.%m.%d")

def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list

def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    end_date = today + timedelta(days=days)
    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        
        if today <= birthday_this_year <= end_date:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": date_to_string(birthday_this_year)
            })

    return upcoming_birthdays

users = [
    {"name": "Sarah Lee", "birthday": "1957.03.30"},
    {"name": "John Doe", "birthday": "1985.03.28"},
    {"name": "Jane Smith", "birthday": "1990.03.27"},
    {"name": "John Doe", "birthday": "1985.01.23"},
]

prepared_users = prepare_user_list(users)
upcoming_birthdays = get_upcoming_birthdays(prepared_users, 7)
print(upcoming_birthdays)
