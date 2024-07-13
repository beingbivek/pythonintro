# Develop a software application for a bank that includes functionalities to add and view customer information.
# Each customer should have an ID, name, phone number, and balance.

import controller as c

usertext = '''
Enter
'1' to add Customer
'2' to view all Customer
'3' to view single customer
'4' to search customer
'5' to delete customer
'6' to update customer
'''

user_input = int(input(usertext))
if user_input == 1:
    c.addProduct()
elif user_input == 2:
    c.viewallproduct()
elif user_input == 3:
    pid = input("Enter product ID: ")
    c.viewsingleproduct(pid)
elif user_input == 4:
    pass
elif user_input == 5:
    pass
elif user_input == 6:
    pass
else: print("Invalid Option")