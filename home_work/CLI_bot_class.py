from collections import UserDict
from datetime import datetime
from def_store import get_upcoming_birthdays


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
            raise ValueError(
                f"Телефонний номер {value} повинен містити рівно 10 цифр!")

        super().__init__(value)


class Birthday(Field):

    def __init__(self, value: str):
        try:
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def __str__(self):

        birthday_str = f", birthday: {self.birthday.value.strftime('%d.%m.%Y')}" if self.birthday else ""
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}{birthday_str}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def add_birthday(self, birth_date: str):

        self.birthday = Birthday(birth_date)

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

        return get_upcoming_birthdays(self.data)


if __name__ == '__main__':

    book = AddressBook()

    rec1 = Record("Kolya")
    rec1.add_phone('0666985192')
    rec1.add_phone('0676466593')
    rec1.add_birthday('13.03.1984')

    book.add_record(rec1)

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("15.3.1989")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    print(book.get_congrats())
