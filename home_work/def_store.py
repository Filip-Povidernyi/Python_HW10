from datetime import datetime, timedelta


def get_upcoming_birthdays(data: dict) -> list:

    upcoming_birthdays_list = []
    today = datetime.now().date()

    for key, item in data.items():

        if item.birthday is None:
            continue

        birthday_date = item.birthday.value

        if (today.month == 12) and (datetime(birthday_date.year, 1, 1).date() <= birthday_date < datetime(birthday_date.year, 1, 7).date()):

            birthday_date_this_year = datetime(
                year=(today.year + 1), month=birthday_date.month, day=birthday_date.day).date()

        else:

            birthday_date_this_year = datetime(
                year=today.year, month=birthday_date.month, day=birthday_date.day).date()

        if birthday_date_this_year < today:

            print(birthday_date_this_year)

        if today <= birthday_date_this_year <= (today + timedelta(days=6)):

            if birthday_date_this_year.weekday() < 5:

                message_dict = {}
                date_in_string = birthday_date_this_year.strftime(
                    "%d.%m.%Y")
                message_dict.update(
                    {'name': key, 'congratulation_date': date_in_string})
                upcoming_birthdays_list.append(message_dict)

            else:

                message_dict = {}
                date_in_string = (birthday_date_this_year + timedelta(
                    days=(7 - birthday_date_this_year.weekday()))).strftime("%d.%m.%Y")
                message_dict.update(
                    {'name': key, 'congratulation_date': date_in_string})
                upcoming_birthdays_list.append(message_dict)

    return upcoming_birthdays_list
