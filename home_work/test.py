from datetime import datetime


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Birthday(Field):
    def __init__(self, value):
        try:
            # Перетворюємо рядок у об'єкт datetime
            self.value = datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


# Приклад використання

bday = Birthday("29.02.2023")  # Неправильна дата (немає 29 лютого 2023)
print(bday)

bday2 = Birthday("15.08.1995")  # Коректна дата
print(bday2)
