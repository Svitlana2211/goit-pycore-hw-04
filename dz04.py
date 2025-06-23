def parse_input(user_input):
    parts = user_input.strip().split()
    if not parts:
        return "", []
    cmd = parts[0].lower()
    args = parts[1:]
    return cmd, args

def add_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Use: add [name] [phone]")
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    except ValueError as e:
        return f"Error: {e}"

def change_contact(args, contacts):
    try:
        if len(args) != 2:
            raise ValueError("Use: change [name] [new_phone]")
        name, phone = args
        if name not in contacts:
            raise KeyError("Contact not found.")
        contacts[name] = phone
        return "Contact updated."
    except (ValueError, KeyError) as e:
        return f"Error: {e}"

def show_phone(args, contacts):
    try:
        if len(args) != 1:
            raise ValueError("Use: phone [name]")
        name = args[0]
        if name not in contacts:
            raise KeyError("Contact not found.")
        return contacts[name]
    except (ValueError, KeyError) as e:
        return f"Error: {e}"

def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = []
    for name, phone in contacts.items():
        result.append(f"{name}: {phone}")
    return "\n".join(result)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        if not user_input.strip():
            continue

        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
