from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    try:
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        current_date = datetime.today().date()
        delta = (given_date - current_date).days
        return delta
        
    except ValueError:
        raise ValueError(
            'Помилка!! \nНевірно введена дата, використовуйте формат "РРРР-ММ-ДД"'
            )
def start_program():
    user_input = input(
        "Вітаю! \nВведіть дату у форматі РРРР-ММ-ДД: "
        )
    try:
        user_days = get_days_from_today(user_input)
        if user_days > 0:
            print(
                f"Залишилось {user_days} днів."
                )
        elif user_days < 0:
            print(
                f"З того моменту пройшло... \n{abs(user_days)} днів."
                )
        else:
            print(
                "Молодець! \nЦе сьогоднішній день!"
                )
    except ValueError as error:
        print(error)

start_program()
