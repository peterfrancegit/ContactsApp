class ContactList:
    def __init__(self):
        self.contact_list = []

    def showContacts(self, contact_list):
        print("----------------------------------------------------")
        for contact in contact_list:
            print("Name:   " + contact["lname"] + ", " + contact["fname"])
            print("Number: " + contact["number"])
            print("----------------------------------------------------")

    def addContact(self, contact_list, contact):
        contact_list.append(contact)

## Sorts alphabetically by last name, then first name
    def sortContacts(self, contact_list):
        self.contact_list = sorted(contact_list, key = lambda i: (i["lname"], i["fname"]))

## For finding a contact. Will first consider last name
    def findContactByLname(self, contact_list, lname):
        shortlist = []
        for contact in contact_list:
            if contact["lname"] == lname:
                shortlist.append(contact)
        return shortlist

## If last name is not unique then considers first name
    def findContactByFname(self, contact_list, fname):
        shortlist = []
        for contact in contact_list:
            if contact["fname"] == fname:
                shortlist.append(contact)
        return shortlist

## If full name is not unique then considers number
    def findContactByNumber(self, contact_list, number):
        shortlist = []
        for contact in contact_list:
            if contact["number"] == number:
                shortlist.append(contact)
        return shortlist

    def editContact(self, contact_list, contact, field, new_info):
        for curr_contact in contact_list:
            if curr_contact == contact:
                curr_contact[field] = new_info

    def delContact(self, contact_list, contact):
        for curr_contact in contact_list:
            if curr_contact == contact:
                contact_list.remove(curr_contact)