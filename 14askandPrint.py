# Write a Python program that asks the user to enter the names of n people, then prints all names that start with the letter 'B', and if no such names are found, it should display "No Name Found"

# Ask number of users
total_users = int(input("Enter total no. of users: "))
names = []

# Ask names to user and add to names list
for i in range(total_users):
    names.append(input(f"Enter Name {i+1}: "))

# Using List Comprehension get names starting with 'B'
b_names = [name for name in names if name.upper().startswith('B')]

print("\n-----------------\n")
# Print all names that starts with letter 'B'
# and if there's no name than display "No Name Found"
if b_names != []:
    for bname in b_names:
        print(bname)
elif b_names == []:
    print("No Name Found")
else:
    print("Something went wrong!")
