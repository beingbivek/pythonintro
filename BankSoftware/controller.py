import csv
import os
from customer import Customer
import filecontroller as fc

update_user_text = '''
What do you want to update:
'1' to update id
'2' to update name
'3' to update phone
'4' to update balance
'5' to update citizenship no
Enter any other keys to cancel update
'''

def search_customer_by_id(sid,list):
    for customer in list:
        if customer.i == sid:
            return customer
    return None

def addcustomer():
    noofcust = int(input("Enter no's of customers to add: "))
    new_customer = []
    i = 0
    while i < noofcust:
        c = Customer(id="",name="",phone="",balance="",ctzno="")
        c.i = input(f"Enter Customer {i+1} ID: ")
        if search_customer_by_id(c.i) == None:
            c.n = input(f"Enter Customer {i+1} Name: ")
            c.p = input(f"Enter Customer {i+1} Phone Number: ")
            c.b = input(f"Enter Customer {i+1} Balance: ")
            c.c = input(f"Enter Customer {i+1} Citizenship No.: ")
            new_customer.append(c)
            i+=1
        else: print(f"{c.i} ID is already used. use different ID")
    fc.convert_list_to_csv(new_customer)
    print("Customers Added Successfully!")

def viewallcustomer():
    print("View All Customers: \n-------------")
    for data in fc.convert_csv_to_list():
        data.displaycustomer()
    print("\n-------------\n")

def viewsinglecustomer(cid):
    singlecustomer = search_customer_by_id(cid,fc.convert_csv_to_list())
    if singlecustomer != None:
        singlecustomer.displaycustomer()
    else: print("No such customer found.")
        
def searchcustomerbyname(cname):
    for data in fc.convert_csv_to_list():
        if data.n.lower() == cname.lower():
            customer = data
            break
        else:
            customer = None
    if customer != None:
        customer.displaycustomer()
    else: print("No such customer found.")

def deletecustomer(cid):
    updated_customer = []
    deleting_customer = None
    for data in fc.convert_csv_to_list():
        if data.i == cid:
            deleting_customer = data
        else:
            updated_customer.append(data)
    if deleting_customer != None:
        decision = input(f"Are you sure you want to delete '{deleting_customer.i}''{deleting_customer.n}'? (Y/N): ")
        if decision.lower() == "y" :
            os.remove(fc.filelocation)
            fc.convert_list_to_csv(updated_customer)
            print("Deleted Successfully!")
        else: print("Deletion Cancelled!")
    else: print("No such customer found.")

def updatecustomer(uid):
    all_customers = fc.convert_csv_to_list()
    customer_to_update = search_customer_by_id(uid,all_customers)
    index = all_customers.index(customer_to_update)
    if customer_to_update != None:
        customer_to_update.displaycustomer()
        user_input = input(update_user_text)
        if user_input == '1':
            value = input("Enter new ID: ")
            if search_customer_by_id(value) == None:
                customer_to_update.i = value
                update_value_of_customer(all_customers,index,customer_to_update)
            else: print("ID can't be repeated!")
        elif user_input == '2': value = input("Enter Customer Name: "); customer_to_update.n = value ; update_value_of_customer(all_customers,index,customer_to_update)
        elif user_input == '3': value = input("Enter new Phone No.: "); customer_to_update.p = value ; update_value_of_customer(all_customers,index,customer_to_update)
        elif user_input == '4': value = input("Enter Balance: "); customer_to_update.b = value ; update_value_of_customer(all_customers,index,customer_to_update)
        elif user_input == '5': value = input("Enter Citizenship No: "); customer_to_update.c = value ; update_value_of_customer(all_customers,index,customer_to_update)
        else: print("Update is cancelled.")
    else: print("Can't Find Costumer to update.")
        
def update_value_of_customer(a,i,u):
    a[i] = u
    os.remove(fc.filelocation)
    fc.convert_list_to_csv(a)
    print('Successfully Updated!')
            