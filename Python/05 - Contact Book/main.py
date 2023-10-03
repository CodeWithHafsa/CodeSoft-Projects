class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contact_list(self):
        for contact in self.contacts:
            print(f"Name: {contact.name}")
            print(f"Phone Number: {contact.phone_number}")
            print(f"Email: {contact.email}")
            print(f"Address: {contact.address}")
            print()

    def search_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                print(f"Name: {contact.name}")
                print(f"Phone Number: {contact.phone_number}")
                print(f"Email: {contact.email}")
                print(f"Address: {contact.address}")
                print()

    def update_contact(self, search_term):
        for contact in self.contacts:
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                new_name = input("Enter new name (leave blank to keep current): ")
                new_phone_number = input("Enter new phone number (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_address = input("Enter new address (leave blank to keep current): ")

                if new_name:
                    contact.name = new_name
                if new_phone_number:
                    contact.phone_number = new_phone_number
                if new_email:
                    contact.email = new_email
                if new_address:
                    contact.address = new_address

    def delete_contact(self, search_term):
        for i, contact in enumerate(self.contacts):
            if search_term.lower() in contact.name.lower() or search_term in contact.phone_number:
                del self.contacts[i]
                break

# Example usage
contact_manager = ContactManager()

# Add contacts
contact_manager.add_contact(Contact("John Doe", "1234567890", "john.doe@example.com", "123 Main St"))
contact_manager.add_contact(Contact("Jane Smith", "0987654321", "jane.smith@example.com", "456 Elm St"))

# View all contacts
print("All Contacts:")
contact_manager.view_contact_list()

# Search for a specific contact
print("Search Results:")
contact_manager.search_contact("John")

# Update a contact
print("Updated Contact:")
contact_manager.update_contact("John Doe")
contact_manager.view_contact_list()

# Delete a contact
print("Deleted Contact:")
contact_manager.delete_contact("Jane Smith")
contact_manager.view_contact_list()
