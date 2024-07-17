# Develop a software application for a bank that includes functionalities to add and view customer information.
# Each customer should have an ID, name, phone number, and balance.

import controller as c

usertext = '''
Welcome to Bank Customer
Enter
'1' to add Customer
'2' to view all Customer
'3' to view single customer
'4' to search customer via name
'5' to delete customer
'6' to update customer
'''

user_input = int(input(usertext))
if user_input == 1:
    c.addcustomer()
elif user_input == 2:
    c.viewallcustomer()
elif user_input == 3:
    cid = input("Enter Customer ID: ")
    c.viewsinglecustomer(cid)
elif user_input == 4:
    cname = input("Enter Customer Name: ")
    c.searchcustomerbyname(cname)
elif user_input == 5:
    cid = input("Enter Customer ID to delete: ")
    c.deletecustomer(cid)
elif user_input == 6:
    uid = input("Enter Customer ID to update: ")
    c.updatecustomer(uid)
else: print("Invalid Option")