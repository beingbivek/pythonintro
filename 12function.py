# Function: A set of code that perform certain task
# Imp: We need to call a function
# def function_name():
#     function code

# Define Function
# def displayName():
#     print("My name is Bivek Thapa")

# # Calling Function
# displayName()

# # Create a function that display your address.
# def myAddress():
#     print("My address is Koteshwor")

# myAddress()

# # WAP to print even number between start and end using funciton

# start = 100
# end = 150

# def display_even(first, last):
#     for i in range(first,last+1,2):
#         print(i)

# display_even(start,end)

# Types of Function:
# System Define
# User Define
# If there is nothing inside (), it is called no parameter
# If there is no return statement, it is called no return

# 1. No parameter and no return type
# 2. parameter and no return type
# 3. parameter and return type
# 4. No parameter and return type

# 1. type
def myAddress():
    print("My address is Koteshwor")

myAddress()

# 2. type
def add(n1,n2): # here n1,n2 are parameters
    total = n1 + n2
    print(f"total is {total}")

add(50,60) # here 50,60 are arguments

# 3. type
def find_cube(number):
    cube = number ** 3
    return cube

myvalue = find_cube(2) # return should be called and assigned to a value.
print(myvalue)

# 4. type
def minvoter_age():
    return 18

print(minvoter_age())

