import csv
from customer import Customer

filelocation = './17Bank/customer.csv'


def writeFile(data):
    f = open(filelocation,'a')
    f.write(data)
    f.close()

# def readFile(): # This is also a right way
#     f = open(filelocation,'r')
#     fileData = f.read().splitlines()
#     f.close()
#     return fileData

def readFile(): # This is efficient way using Class and CSV
    all_customer = []
    with open(filelocation,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            c = Customer(id=row[0],name=row[1],phone=row[2],balance=row[3],ctzno=row[4])
            all_customer.append(c)
    return all_customer

def addProduct():
    newpronum = int(input("Enter no's of products to add: "))
    for i in range(newpronum):
        c = Customer(id="",name="",phone="",balance="")
        c.i = input(f"Enter Customer {i+1} ID: ")
        c.n = input(f"Enter Customer {i+1} Name: ")
        c.p = input(f"Enter Customer {i+1} Phone Number: ")
        c.b = input(f"Enter Customer {i+1} Balance: ")
        c.c = input(f"Enter Customer {i+1} Citizenship No.: ")
        writeFile(f"{c.i},{c.n},{c.p},{c.b},{c.c}\n")

def viewallproduct():
    print("View All Customers: \n-------------")
    for data in readFile():
        data.displayproduct()
    print("\n-------------\n")

def viewsingleproduct(pid):
    for data in readFile():
        if data.i == pid:
            product = data
            break
        else:
            product = None
    if product != None:
        product.displayproduct()
    else: print("No such product found.")
        