import json
import os

CONTACTS_FILE = "contacts.json"


def load_contacts():
    """Load contacts from JSON file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r") as f:
        return json.load(f)


def save_contacts(contacts):
    """Save contacts to JSON file."""
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)

    print("\nContact added successfully!\n")


def view_contacts():
    contacts = load_contacts()

    if not contacts:
        print("\nNo contacts found.\n")
        return

    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()


def search_contacts():
    contacts = load_contacts()
    keyword = input("Search by name or phone: ").lower()

    # results = [
    #     c for c in contacts    '''or its same as results = []
    #                                for c in contacts:
    #                                results.append(c)'''
      
    #     if keyword in c["name"].lower() or keyword in c["phone"]
    # ]
    
    #or
    
    results = []

    for c in contacts:
     if keyword in c["name"].lower() or keyword in c["phone"]:
        results.append(c)


    if not results:
        print("\nNo matching contacts.\n")
        return

    print("\n--- Search Results ---")
    for c in results:
        print(f"{c['name']} - {c['phone']} - {c['email']}")
    print()


def update_contact():
    contacts = load_contacts()
    view_contacts()

    if not contacts:
        return

    try:
        index = int(input("Enter contact number to update: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid selection.\n")
            return
    except ValueError:
        print("Please enter a valid number.\n")
        return

    print("\nLeave field empty to keep current value.\n")

    name = input(f"New name ({contacts[index]['name']}): ").strip()
    phone = input(f"New phone ({contacts[index]['phone']}): ").strip()
    email = input(f"New email ({contacts[index]['email']}): ").strip()

    if name:
        contacts[index]["name"] = name
    if phone:
        contacts[index]["phone"] = phone
    if email:
        contacts[index]["email"] = email

    save_contacts(contacts)
    print("\nContact updated successfully!\n")


def delete_contact():
    contacts = load_contacts()
    view_contacts()

    if not contacts:
        return

    try:
        index = int(input("Enter contact number to delete: ")) - 1
        if index < 0 or index >= len(contacts):
            print("Invalid selection.\n")
            return
    except ValueError:
        print("Please enter a valid number.\n")
        return

    deleted = contacts.pop(index)
    save_contacts(contacts)

    print(f"\nDeleted contact: {deleted['name']}\n")


def menu():
    while True:
        print("=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


if __name__ == "__main__":
    menu()
