import csv
from customer import Customer
import os

filelocation = './BankSoftware/customer.csv'


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

def addcustomer():
    noofcust = int(input("Enter no's of customers to add: "))
    for i in range(noofcust):
        c = Customer(id="",name="",phone="",balance="",ctzno="")
        c.i = input(f"Enter Customer {i+1} ID: ")
        c.n = input(f"Enter Customer {i+1} Name: ")
        c.p = input(f"Enter Customer {i+1} Phone Number: ")
        c.b = input(f"Enter Customer {i+1} Balance: ")
        c.c = input(f"Enter Customer {i+1} Citizenship No.: ")
        writeFile(f"{c.i},{c.n},{c.p},{c.b},{c.c}\n")

def viewallcustomer():
    print("View All Customers: \n-------------")
    for data in readFile():
        data.displaycustomer()
    print("\n-------------\n")

def viewsinglecustomer(cid):
    for data in readFile():
        if data.i == cid:
            customer = data
            break
        else:
            customer = None
    if customer != None:
        customer.displaycustomer()
    else: print("No such customer found.")
        
def searchcustomerbyname(cname):
    for data in readFile():
        if data.n.lower() == cname.lower():
            customer = data
            break
        else:
            customer = None
    if customer != None:
        customer.displaycustomer()
    else: print("No such customer found.")

def deletecustomer(cid):
    customer = []
    for data in readFile():
        if data.i == cid:
            cust = data
        else:
            customer.append(data)
    if cust != None:
        decision = input(f"Are you sure you want to delete '{cust.i}''{cust.n}'? (Y/N): ")
        if decision.lower() == "y" :
            os.remove(filelocation)
            for c in customer:
                # print(c)
                writeFile(f"{c.i},{c.n},{c.p},{c.b},{c.c}\n")
        else: print("Deletion Cancelled:")
    else: print("No such customer found.")