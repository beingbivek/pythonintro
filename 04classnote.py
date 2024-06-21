# Strings

# name = "bivek Thapa"

# print(name.capitalize())
# print(name.upper())
# print(name.lower())

# # To calculate total no. of words
# splitname = name.split(" ") # space or comma or any character can be use to split, split creates an array/list
# print(len(splitname))

# # To get first and last name
# print(f"First name is {splitname[0]}")
# print(f"Last name is {splitname[1]}")

# for loop in list
# todo_list = ['Learn python','sell house','do homework']
# todo_list.append("Listen to audiobook")
# todo_list[2] = 'goto gym'

# for i in todo_list:
#     print(i)

# fruits = ('Apple','Mango','Orange')

# for i in fruits:
#     print(i)

# Dictionary , key value pair
# expenses = {
#     'sunday' : 1000,
#     'monday' : 1000,
#     'tuesday' : 1000,
#     'wednesday' : 1000,
#     'thursday' : 1000,
#     'friday' : 1000,
#     'saturday' : 1000,
# }

# print(f"Friday expenses is {expenses['friday']}")
# total = sum(expenses.values())
# print(f"Total expenses is {total}")
# print(f"Average expenses is {total/7}")

# For Loop
# for i in range(10): # i starts from 0
#     print(i+1) # gives output of numbers from 1 to 10

# Dictionary in loops using k, v
country_capital = {
    'Nepal' : 'Kathmandu',
    'US' : 'Washinton DC',
    'Japan' : 'Tokyo',
    'India' : 'New Delhi'
}

for k in country_capital:
    print(f"Capital city of {k} is {country_capital[k]}")

# String Loop
# for i in country_capital['Nepal']:
#     print(i)

# Keys only and sorting and reverse sorting
all_key = list(country_capital.keys())
all_key.sort()
print(all_key)
all_key.reverse()
print(all_key)