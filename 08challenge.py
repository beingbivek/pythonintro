# Write a Python program that prompts the user to enter a number corresponding to a month (1 for January, 2 for February, ..., 12 for December). The program should then display the name of the month based on the number entered.

u = int(input("Enter 1 to run Fast way and 2 to run Long Way: "))
# Fast Way

if u == 1:
    mon_num = int(input("Enter Month Number [1-12]: "))
    month = ['Janaury','Febuarary','March','April','May','June','July','August','September','October','November','December']

    if mon_num >= 1 and mon_num <= 12:
        print(f"Your corresponding day is {month[mon_num - 1]}")
    else:
        print("Please enter numbers between 1-12, and try again")

# Long Way

elif u == 2:
    mon_num = int(input("Enter Month Number [1-12]: "))
    if mon_num == 1:
        print("Corresponding Month is Janaury.")
    elif mon_num == 2:
        print("Corresponding Month is Febraury.")
    elif mon_num == 3:
        print("Corresponding Month is March.")
    elif mon_num == 4:
        print("Corresponding Month is April.")
    elif mon_num == 5:
        print("Corresponding Month is May.")
    elif mon_num == 6:
        print("Corresponding Month is June.")
    elif mon_num == 7:
        print("Corresponding Month is July.")
    elif mon_num == 8:
        print("Corresponding Month is August.")
    elif mon_num == 9:
        print("Corresponding Month is September.")
    elif mon_num == 10:
        print("Corresponding Month is October.")
    elif mon_num == 11:
        print("Corresponding Month is November.")
    elif mon_num == 12:
        print("Corresponding Month is December.")
    else:
        print("Invalid Option")

else:
    print("Invalid Option")
