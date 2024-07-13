class Customer:
    def __init__(self, id, name, phone, balance, ctzno):
        self.i = id
        self.n = name
        self.p = phone
        self.b = balance
        self.c = ctzno

    def displaycustomer(self):
        print(f"{self.i},{self.n},{self.p},{self.b},{self.c}\n")