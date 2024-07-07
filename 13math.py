# # Create funtion to find square root using math
# import math

# sq = math.sqrt(25)

# number = 3.12341234
# print(f"Number is {number:2f} and {sq}")

# n1 = math.ceil(10.1) # to get upper integer
# n2 = math.floor(10.3) # to get lower integer
# print(n1)
# print(n2)

# n3 = math.pow(2,3) # 2 ko power 3
# print(n3)

# print(round(10.6)) # to get round value

# # WAP to ask user decimal value and round its value
def round_number(n):
    return round(n)

user_input = float(input("Enter any decimal number to round it: "))
print(round_number(user_input))