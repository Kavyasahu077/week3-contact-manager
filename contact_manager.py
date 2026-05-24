# ==========================================
# Name: Kavya Sahu
# Project: Contact Management System
# ==========================================

import json
import re

FILE_NAME = "contacts_data.json"


# Load contacts from file
def load_contacts():

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)

    except:
        return {}


# Save contacts to file
def save_contacts(contacts):

    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


# Validate phone number
def validate_phone(phone):

    digits = re.sub(r"\D", "", phone)

    return len(digits) >= 10


# Add contact
def add_contact(contacts):

    print("\n--- ADD CONTACT ---")

    name = input("Enter name: ").strip().title()

    if name == "":
        print("Name cannot be empty!")
        return

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()

    if not validate_phone(phone):
        print("Invalid phone number!")
        return

    email = input("Enter email: ").strip()
    group = input("Enter group (Friends/Family/Work): ").strip().title()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "group": group
    }

    save_contacts(contacts)

    print("Contact added successfully!")


# View all contacts
def view_contacts(contacts):

    print("\n--- ALL CONTACTS ---")

    if not contacts:
        print("No contacts found!")
        return

    for name, info in contacts.items():

        print("-" * 40)

        print(f"Name   : {name}")
        print(f"Phone  : {info['phone']}")
        print(f"Email  : {info['email']}")
        print(f"Group  : {info['group']}")


# Search contact
def search_contact(contacts):

    search = input("Enter name to search: ").strip().lower()

    found = False

    for name, info in contacts.items():

        if search in name.lower():

            found = True

            print("\nContact Found")
            print("-" * 40)

            print(f"Name   : {name}")
            print(f"Phone  : {info['phone']}")
            print(f"Email  : {info['email']}")
            print(f"Group  : {info['group']}")

    if not found:
        print("No matching contact found!")


# Update contact
def update_contact(contacts):

    name = input("Enter contact name to update: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    new_phone = input("Enter new phone number: ").strip()

    if validate_phone(new_phone):
        contacts[name]["phone"] = new_phone

    new_email = input("Enter new email: ").strip()

    if new_email:
        contacts[name]["email"] = new_email

    save_contacts(contacts)

    print("Contact updated successfully!")


# Delete contact
def delete_contact(contacts):

    name = input("Enter contact name to delete: ").strip().title()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input("Are you sure? (yes/no): ").lower()

    if confirm == "yes":

        del contacts[name]

        save_contacts(contacts)

        print("Contact deleted successfully!")


# Contact statistics
def show_statistics(contacts):

    print("\n--- CONTACT STATISTICS ---")

    print(f"Total Contacts: {len(contacts)}")

    groups = {}

    for info in contacts.values():

        group = info["group"]

        groups[group] = groups.get(group, 0) + 1

    print("\nContacts by Group:")

    for group, count in groups.items():

        print(f"{group}: {count}")


# Main Menu
def main():

    contacts = load_contacts()

    while True:

        print("\n" + "=" * 50)
        print("      CONTACT MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. View Statistics")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact(contacts)

        elif choice == "2":
            search_contact(contacts)

        elif choice == "3":
            update_contact(contacts)

        elif choice == "4":
            delete_contact(contacts)

        elif choice == "5":
            view_contacts(contacts)

        elif choice == "6":
            show_statistics(contacts)

        elif choice == "7":

            print("\nThank you for using Contact Manager!")
            break

        else:
            print("Invalid choice! Please try again.")


# Run Program
if __name__ == "__main__":
    main()