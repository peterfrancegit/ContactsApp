from Contact import *
from ContactList import *

toExit = False
myContacts = ContactList()

while not toExit:
    print("What would you like to do?")
    print("1) Add a contact;  2) Edit a contact;  3) Delete a contact;  4) List contacts;  5) Exit")
    choice = input("Choose 1, 2, 3, 4 or 5:  ")
    if choice == "5":
        toExit = True
    elif choice == "1":
        fname = input("What is the contact's first name? ")
        lname = input("What is the contact's last name? ")
        number = input("What is the contact's phone number? ")
        duplicate = False
        for contact in myContacts.contact_list:
            ## phone number must be unique in contact list
            if contact.number == number:
                print("This number is already assigned")
                duplicate = True
                break
        if not duplicate:
            myContacts.add_contact(Contact(fname, lname, number))
    elif choice in ["2", "3", "4"]:
        ## Also displays contacts if you choose to edit or delete
        if len(myContacts.contact_list) == 0:
            print("You have zero contacts")
        else:
            print("Here are your contacts:")
            myContacts.sort_contacts()
            myContacts.show_contacts()
            if choice in ["2", "3"]:
                print("Choose which contact?")
                isReal = True
                lname = input("What is their last name? ")
                possibles = myContacts.find_contact_by_lname(lname)
                if len(possibles) == 0:
                    print("There is no such contact")
                    isReal = False
                elif len(possibles) == 1:
                    contact = possibles[0]
                else:
                    fname = input("What is their first name? ")
                    possibles = myContacts.find_contact_by_fname(fname)
                    if len(possibles) == 0:
                        print("There is no such contact")
                        isReal = False
                    elif len(possibles) == 1:
                        contact = possibles[0]
                    else:
                        number = input("What is their number? ")
                        possibles = myContacts.find_contact_by_number(number)
                        if len(possibles) == 0:
                            print("There is no such contact")
                            isReal = False
                        else:
                            contact = possibles[0]
                ## Contact must exist to edit or delete
                if isReal:
                    if choice == "3":
                        myContacts.delete_contact(contact)
                    else:
                        print("Which field would you like to edit?")
                        print("1) First name;  2) Last name;  3) Phone number")
                        choice = input("Choose 1, 2, or 3:  ")
                        if choice == "1":
                            field = "first name"
                        elif choice == "2":
                            field = "last name"
                        elif choice == "3":
                            field = "phone number"
                        print(f"Edit {field}")
                        print("What would you like to change this to?")
                        new_info = input("> ")
                        myContacts.edit_contact(contact, field, new_info)
