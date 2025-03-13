from collections import UserDict
from datetime import datetime, timedelta


class Field:

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, value: str):

        if len(value) != 10 or not value.isdigit():
            raise ValueError()

        super().__init__(value)


class Birthday(Field):

    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError(
                f'Invalid date format. Use DD.MM.YYYY\n'f"Or day {value} is out of range for month")


class Record:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):

        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value.title()}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def add_birthday(self, birth_date: str):

        self.birthday = Birthday(birth_date)
        return f"{self.birthday.value.strftime('%d.%m.%Y')} added"

    def remove_phone(self, rem_phone: str):

        self.phones = [
            phone for phone in self.phones if phone.value != rem_phone]

    def edit_phone(self, old_phone: str, new_phone: str):

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).value

                return f"Номер {old_phone} змінено на номер {new_phone}"

        raise ValueError(f"Номер {old_phone} не знайдено")

    def find_phone(self, f_phone: str):

        for phone in self.phones:
            if phone.value == f_phone:
                return phone

        return None


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
