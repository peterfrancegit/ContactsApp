class Contact:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number

    def edit(self, field, new_value):
        if field == 'FNAME':
            self.fname = new_value
        elif field == 'LNAME':
            self.lname = new_value
        elif field == 'NUMBER':
            self.number = new_value
