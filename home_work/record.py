from birthday import Birthday
from name import Name
from phone import Phone


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
