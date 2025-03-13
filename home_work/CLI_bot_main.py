from pathlib import Path
import pickle
from handler import command_parser, add_contact, show_phone, show_all, change_contact, add_birthday, show_birthday, birthdays
from CLI_bot_class import AddressBook


def main():

    print("Welcome to the assistant bot!")

    path = Path('contacts.pkl')

    if path.exists() and path.is_file():

        with open('contacts.pkl', 'rb') as file:
            book = pickle.load(file)
    else:
        book = AddressBook()

    while True:

        command = input("Enter a command: ").strip().lower()
        cmd, args = command_parser(command)

        match cmd:

            case "hello":
                print("How can I help you?")

            case "add":
                print(add_contact(args, book))

            case "change":
                print(change_contact(args, book))

            case "phone":
                print(show_phone(args, book))

            case "all":
                show_all(book)

            case "add-birthday":
                print(add_birthday(args, book))

            case "show-birthday":
                print(show_birthday(args, book))

            case "birthdays":
                if isinstance(birthdays(book), list):
                    print(f"Список привітань на цьому тижні:\n" +
                          "\n".join(str(birthday) for birthday in birthdays(book)))
                else:
                    print(birthdays(book))

            case "exit":
                with open('contacts.pkl', 'wb') as file:
                    pickle.dump(book, file)
                print("Good bye!")
                break

            case "close":
                with open('contacts.pkl', 'wb') as file:
                    pickle.dump(book, file)
                print("Good bye!")
                break

            case _:
                print("Invalid command.")


if __name__ == "__main__":
    main()
