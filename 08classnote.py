# Conditions
# import datetime
# # Voter or Not
# birth_year = int(input("Enter birth Year: "))
# age = datetime.date.today().year
# # print(age)

# if age >= 18:
#     print("You are a Voter")
# else:
#     print("You are not a voter")

# # Ask user to enter price, if price is >= 500, print it is expensive else price is good

# price = int(input("Enter Price: "))

# if price >= 500:
#     print("The item is Expensive!")
# else:
#     print("Price of the item is good.")

# # Ask user to enter number and find that number is odd or even

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Number is Even")
# else:
#     print("Number is odd")

# # Find biggest number

# n1 = int(input("Enter Number 1: "))
# n2 = int(input("Enter Number 2: "))
# n3 = int(input("Enter Number 3: "))

# if n1 > n2 and n1 > n3:
#     print(f"{n1} is the biggest number")
# elif n2 > n1 and n2 > n3:
#     print(f"{n2} is the biggest number")
# elif n3 > n1 and n3 > n2:
#     print(f"{n3} is the biggest number")
# else:
#     print("All are equal")

# Always use elif for all conditions and use else for uncertain conditions.

# Find day with numbers [1-7]

day_num = int(input("Enter Number [1-7]: ")) - 1
day = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']

if day_num >= 0 and day_num <= 6:
    print(f"Your corresponding day is {day[day_num]}")
else:
    print("Please enter numbers between 1-7, and try again")