from Contact import *
from ContactList import *

toExit = False
myContacts = ContactList()

while toExit == False:
    print("What would you like to do?")
    print("1) Add a contact;  2) Edit a contact;  3) Delete a contact;  4) List contacts;  5) Exit")
    choice = input("Choose 1, 2, 3, 4 or 5:  ")
    if choice == "5":
        toExit = True
    elif choice == "1":
        fname = input("What is the contacts first name? ")
        lname = input("What is the contacts last name? ")
        number = input("What is the contacts number? ")
        duplicate = False
        for curr_contact in myContacts.contact_list:
        ## phone number must be unique in contact list
            if curr_contact["number"] == number:
                print("This number is already assigned")
                duplicate = True
        if duplicate == False:
            contact = Contact(fname, lname, number)
            contact.makeEntry(contact.fname, contact.lname, contact.number)
            myContacts.addContact(myContacts.contact_list, contact.entry)
    elif choice in ["2", "3", "4"]:
        ## Also displays contacts if you choose to edit or delete
        if len(myContacts.contact_list) == 0:
            print("You have zero contacts")
        else:
            print("Here are your contacts:")
            myContacts.sortContacts(myContacts.contact_list)
            myContacts.showContacts(myContacts.contact_list)
            if choice in ["2", "3"]:
                print("Choose which contact?")
                isReal = True
                lname = input("What is their last name? ")
                possibles = myContacts.findContactByLname(myContacts.contact_list, lname)
                if len(possibles) == 0:
                    print("There is no such contact")
                    isReal = False
                elif len(possibles) == 1:
                    contact = possibles[0]
                else:
                    fname = input("What is their first name? ")
                    possibles = myContacts.findContactByFname(possibles, fname)
                    if len(possibles) == 0:
                        print("There is no such contact")
                        isReal = False
                    elif len(possibles) == 1:
                        contact = possibles[0]
                    else:
                        number = input("What is their number? ")
                        possibles = myContacts.findContactByNumber(possibles, number)
                        if len(possibles) == 0:
                            print("There is no such contact")
                            isReal = False
                        else:
                            contact = possibles[0]
                ## Contact must exist to edit or delete
                if isReal == True:
                    if choice == "3":
                        myContacts.delContact(myContacts.contact_list, contact)
                    else:
                        print("Which field would you like to edit?")
                        print("Choose from: fname, lname or number")
                        field = input("> ")
                        print("The current " + field + " is " + contact[field])
                        print("What would you like to change this to?")
                        new_info = input("> ")
                        myContacts.editContact(myContacts.contact_list, contact, field, new_info)