import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    if not os.path.exists(CONTACT_FILE):
        return[]
    with open(CONTACT_FILE, "r") as f:
     return json.load(f)
 
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
         json.dump(contacts, f, indent=5 )
         
def add_contacts():
    contacts = load_contacts()
    name = input("enter contact name : ").strip()
    phone = input("enter contact number : ").strip()
    email = input("enter contact email : ").strip()
    
    contacts.append({"name": name, "phone" : phone, "email" : email})
    save_contacts(contacts)
    print("\n contact added successfully")
    
def view_contacts():
     contacts = load_contacts()
     if not contacts:
         print("no contacts found \n")
         return
     print("====contact list =====")
     for i, contact in enumerate(contacts,1):
         print(f"{i}. {contact['name']} {contact['phone']} {contact['email']}")  
         print()
def delete_contacts():
    contacts = load_contacts()
    
    if not contacts:
        print("No contacts to delete.\n")
        return

    # Show contacts so user can choose
    for i, c in enumerate(contacts, start=1):
        print(f"{i}. {c['name']} - {c['phone']} - {c['email']}")

    try:
        index = int(input("Enter number to delete: "))
    except ValueError:
        print("Please enter a valid number.\n")
        return

    if 1 <= index <= len(contacts):
        removed = contacts.pop(index - 1)
        save_contacts(contacts)
        print(f"Deleted: {removed['name']} ({removed['phone']}) {removed['email']}\n")
    else:
        print("Invalid number.\n")

def search_contacts():
    contacts = load_contacts()
    keyword = input("Search by name, phone, or email: ").lower()

    # results = [
    #     c for c in contacts
    #     if keyword in c["name"].lower()
    #     or keyword in str (c["phone"])
    #     or keyword in c["email"].lower()
    # ]
    
    #or 
    
    results = []
    for c in contacts:
     if keyword in c["name"].lower() or keyword in str(c["phone"]):
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
    

       

        
         
def menu():         
  while True:
    print("======contact Book======")
    print("1. Add contacts")
    print("2. view contacts")
    print("3. search contacts")
    print("4. update contacts")
    print("5. delete contacts")
    print("6. exit")
    
    choice = input("choose an option : ")
    
    if choice == "1":
        add_contacts()
        
    elif choice == "2":
        view_contacts()
        
    elif choice == "3":
        search_contacts()
    elif choice == "4":
        update_contact()
        
    elif choice == "5":
        delete_contacts()
        
    else:
        print("invalid choice")
        
if __name__ == "__main__":
    menu()
    
    
    