
phone_book = {}

def add_contact(name, phone_number):
    """Add a new contact to the phone book."""
    phone_book[name] = phone_number
    print(f"Contact {name} added successfully!")

def remove_contact(name):
    """Remove a contact from the phone book."""
    if name in phone_book:
        del phone_book[name]
        print(f"Contact {name} removed successfully!")
    else:
        print(f"Contact {name} not found!")

def search_contact(name):
    """Search for a contact by name."""
    if name in phone_book:
        print(f"Name: {name}, Phone Number: {phone_book[name]}")
    else:
        print(f"Contact {name} not found!")

def display_contacts():
    """Display all contacts in the phone book."""
    if phone_book:
        print("Phone Book Contacts:")
        for name, number in phone_book.items():
            print(f"Name: {name}, Phone Number: {number}")
    else:
        print("Phone book is empty!")

while True:
    print("\nPhone Book Menu")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Search Contact")
    print("4. Display Contacts")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        name = input("Enter contact name: ")
        phone_number = input("Enter phone number: ")
        add_contact(name, phone_number)
    elif choice == '2':
        name = input("Enter contact name to remove: ")
        remove_contact(name)
    elif choice == '3':
        name = input("Enter contact name to search: ")
        search_contact(name)
    elif choice == '4':
        display_contacts()
    elif choice == '5':
        print("Exiting Phone Book...")
        break
    else:
        print("Invalid choice, please try again.")
