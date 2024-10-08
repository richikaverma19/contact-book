import json
from colorama import init, Fore

# Initialize Colorama
init(autoreset=True)

# File path for storing contacts
FILE_PATH = "contacts.json"

# Load contacts from file
def load_contacts():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_PATH, 'w') as file:
        json.dump(contacts, file)

# Contact book dictionary (loaded from file)
contact_book = load_contacts()

# Function to add a contact
def add_contact():
    name = input(Fore.CYAN + "Enter contact name: " + Fore.WHITE)
    phone = input(Fore.CYAN + "Enter phone number: " + Fore.WHITE)
    email = input(Fore.CYAN + "Enter email address: " + Fore.WHITE)
    
    contact_book[name] = {'Phone': phone, 'Email': email}
    save_contacts(contact_book)
    print(Fore.GREEN + f"Contact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts():
    if contact_book:
        print(Fore.MAGENTA + "\n========== Contact List ==========\n")
        for name, details in contact_book.items():
            print(Fore.CYAN + f"Name: {name}")
            print(Fore.YELLOW + f"Phone: {details['Phone']}")
            print(Fore.YELLOW + f"Email: {details['Email']}\n")
    else:
        print(Fore.RED + "No contacts found!\n")

# Function to update a contact
def update_contact():
    name = input(Fore.CYAN + "Enter the contact name to update: " + Fore.WHITE)
    
    if name in contact_book:
        new_phone = input(Fore.CYAN + "Enter new phone number: " + Fore.WHITE)
        new_email = input(Fore.CYAN + "Enter new email address: " + Fore.WHITE)
        
        contact_book[name] = {'Phone': new_phone, 'Email': new_email}
        save_contacts(contact_book)
        print(Fore.GREEN + f"Contact '{name}' updated successfully!\n")
    else:
        print(Fore.RED + "Contact not found!\n")

# Function to delete a contact
def delete_contact():
    name = input(Fore.CYAN + "Enter the contact name to delete: " + Fore.WHITE)
    
    if name in contact_book:
        confirm = input(Fore.RED + f"Are you sure you want to delete '{name}'? (yes/no): " + Fore.WHITE).lower()
        if confirm == 'yes':
            del contact_book[name]
            save_contacts(contact_book)
            print(Fore.GREEN + f"Contact '{name}' deleted successfully!\n")
    else:
        print(Fore.RED + "Contact not found!\n")

# Function to search for a contact
def search_contact():
    name = input(Fore.CYAN + "Enter the contact name to search: " + Fore.WHITE)
    
    if name in contact_book:
        print(Fore.MAGENTA + f"\nDetails for '{name}':")
        print(Fore.YELLOW + f"Phone: {contact_book[name]['Phone']}")
        print(Fore.YELLOW + f"Email: {contact_book[name]['Email']}\n")
    else:
        print(Fore.RED + "Contact not found!\n")

# Main Menu
def contact_book_menu():
    while True:
        print(Fore.MAGENTA + "\n========== Contact Book Menu ==========\n")
        print(Fore.YELLOW + "1. Add Contact")
        print(Fore.YELLOW + "2. View Contacts")
        print(Fore.YELLOW + "3. Update Contact")
        print(Fore.YELLOW + "4. Delete Contact")
        print(Fore.YELLOW + "5. Search Contact")
        print(Fore.YELLOW + "6. Exit")
        print(Fore.MAGENTA + "=======================================\n")
        
        choice = input(Fore.CYAN + "Choose an option (1-6): " + Fore.WHITE)
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            search_contact()
        elif choice == '6':
            print(Fore.GREEN + "Goodbye! Exiting Contact Book.\n")
            break
        else:
            print(Fore.RED + "Invalid option! Please choose between 1 and 6.\n")

if __name__ == "__main__":
    contact_book_menu()
