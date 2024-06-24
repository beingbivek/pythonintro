# Write a program that generates a username based on user input (e.g., first name, last name, favorite number) and ensures it meets certain criteria.
import random

F_name = input("Enter your First Name: ")
L_name = input("Enter your Last Name: ")
F_number = input("Enter your Favorite Number: ")

# fullname = F_name + L_name + F_number
# nameinlist = []
# username = []
# un = ""

# for i in fullname:
#     nameinlist.append(i)

# print(nameinlist)
# print(random.choice(nameinlist))

print(f"Your username is {F_name + L_name + F_number}")

# for j in range(5):
#     for i in range(8):
#         un = un + random.choice(nameinlist)
#     username.append(un)

# for i in len(username):
#     print(username[i])



