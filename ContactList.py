class ContactList:
    def __init__(self):
        self.contact_list = []

    def show_contacts(self):
        print("----------------------------------------------------")
        for contact in self.contact_list:
            print(f"Name: {contact.lname}, {contact.fname}")
            print(f"Number: {contact.number}")
            print("----------------------------------------------------")

    def add_contact(self, contact):
        self.contact_list.append(contact)

    ## Sorts alphabetically by last name, then first name
    def sort_contacts(self):
        self.contact_list = sorted(self.contact_list, key=lambda i: (i.lname, i.fname))

    ## For finding a contact. Will first consider last name
    def find_contact_by_lname(self, lname):
        shortlist = []
        for contact in self.contact_list:
            if contact.lname == lname:
                shortlist.append(contact)
        return shortlist

    ## If last name is not unique then considers first name
    def find_contact_by_fname(self, fname):
        shortlist = []
        for contact in self.contact_list:
            if contact.fname == fname:
                shortlist.append(contact)
        return shortlist

    ## If full name is not unique then considers number
    def find_contact_by_number(self, number):
        shortlist = []
        for contact in self.contact_list:
            if contact.number == number:
                shortlist.append(contact)
        return shortlist

    def edit_contact(self, contact, field, new_info):
        for curr_contact in self.contact_list:
            if curr_contact == contact:
                curr_contact.field = new_info

    def delete_contact(self, contact):
        for curr_contact in self.contact_list:
            if curr_contact == contact:
                self.contact_list.remove(curr_contact)
