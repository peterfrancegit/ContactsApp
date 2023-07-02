class Contact:
    def __init__(self, fname, lname, number):
        self.fname = fname
        self.lname = lname
        self.number = number
        
## Each contact has its own dictionary for its data
    def makeEntry(self, fname, lname, number):
        self.entry = {"fname": fname, "lname": lname, "number": number}
