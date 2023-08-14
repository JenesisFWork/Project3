#--------------------------------------------------------------------------------------------------------------------------
#Student Name: Jenesis
#Course: CIT 134A
#Term/Year: Fall 2022
#Date: 10/24/2022
#Project Number: 3
#--------------------------------------------------------------------------------------------------------------------------

# Display title
def display_title():
    print("Contact Management System")
    print()
    
# Display menu    
def display_menu():
    print("COMMAND MENU")
    print("list - Display all contacts")
    print("view - View a contact")
    print("add - Add a contact")
    print("delete - Delete a contact")
    print("exit - Exit program")
    print()

# Function to display contacts
def display(contacts):
    i = 1 # Index of first contact
    for contact in contacts:
        print(i , contact)
        i = i + 1

#Functions to view contacts
def view(contacts):
    index = int(input("Which contact to view? "))
    print(contacts[index - 1])   

# Function to add contacts
def add(contacts):
    contact = []
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    idNum = input("Enter id: ")
    contact.append(name)
    contact.append(email)
    contact.append(phone)
    contact.append(idNum)
    contacts.append(contact)

# Function to delete contacts
def delete(contacts):
    index = int(input("Which contact to delete: "))
    del contacts[index - 1]
        
# Main List
def main ():
    contact_list = [["Betty Johnson", "betty.johnson@gmail.com", "(408) 111-2222", "3333"],
                   ["Mark Arlington", "mark.arlington@yahoo.com", "(669) 123-4567", "4444"]]
    # Functions for the menu
    display_title()
    display_menu()
    command = input("Enter your command: ")
    
    while command != "exit": # put strings inside double quotes
        if command == "list":
            # List all contacts
            display(contact_list)
        elif command == "view":
            # View a contact
            view(contact_list)
        elif command == "add":
            # Add a contact
            add(contact_list)
        elif command == "delete":
            # Delete a contact
            delete(contact_list)
        else:
            print("Invalid number. Try again!")
            
        print()
        display_menu()
        command = input("Enter your command: ")
        
    print("Thank you for using my app")
    
main()





