from collections import UserDict
from datetime import datetime, timedelta
from record import Record


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):

        if name in self.data:
            del self.data[name]

    def get_congrats(self):

        upcoming_birthdays_list = []
        today = datetime.now().date()

        for key, item in self.data.items():

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
                        {'name': key.title(), 'congratulation_date': date_in_string})
                    upcoming_birthdays_list.append(message_dict)

                else:

                    message_dict = {}
                    date_in_string_act = birthday_date_this_year.strftime(
                        "%d.%m.%Y")
                    date_in_string = (birthday_date_this_year + timedelta(
                        days=(7 - birthday_date_this_year.weekday()))).strftime("%d.%m.%Y")
                    message_dict.update(
                        {'name': key.title(), 'congratulation_date': date_in_string, 'was': date_in_string_act})
                    upcoming_birthdays_list.append(message_dict)

        if upcoming_birthdays_list:
            return upcoming_birthdays_list
        else:
            return "No birthdays on this week"
