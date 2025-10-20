def parse_input(user_input: str):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd, *args = parts
    return cmd.lower(), args


def add_contact(args, contacts):
    if len(args) != 2:
        return "Usage: add <name> <phone>"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Usage: change <name> <new_phone>"
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Usage: phone <name>"
    name = args[0]
    return contacts.get(name, "Contact not found.")


def show_all(contacts):
    return "\n".join(f"{n}: {p}" for n, p in contacts.items()) or "No contacts found."


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        command, args = parse_input(input("Enter a command: "))

        if command in ("close", "exit"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "":
            continue
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
