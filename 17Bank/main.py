# Develop a software application for a bank that includes functionalities to add and view customer information.
# Each customer should have an ID, name, phone number, and balance.

from customer import Customer

filelocation = './17Bank/customer.csv'

usertext = '''
Enter
'1' to add Customer
'2' to view all Customer
'''

def writeFile(data):
    f = open(filelocation,'a')
    f.write(data)
    f.close()

def readFile():
    f = open(filelocation,'r')
    fileData = f.read().splitlines()
    f.close()
    return fileData

user_input = int(input(usertext))
if user_input == 1:
    newpronum = int(input("Enter no's of products to add: "))
    for i in range(newpronum):
        c = Customer(id="",name="",phone="",balance="")
        c.id = input(f"Enter Customer {i+1} ID: ")
        c.name = input(f"Enter Customer {i+1} Name: ")
        c.phone = input(f"Enter Customer {i+1} Phone Number: ")
        c.balance = input(f"Enter Customer {i+1} Balance: ")
        writeFile(f"{c.id},{c.name},{c.phone},{c.balance}\n")
elif user_input == 2:
    for data in readFile():
        print(data)
