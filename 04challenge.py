# Add your electricity bill from Jan to Dec in Dictionary and Find total and average.

Elec_bill = {
    'Jan' : 2065,
    'Feb' : 2484,
    'Mar' : 2065,
    'Apr' : 2584,
    'May' : 3464,
    'Jun' : 4845,
    'Jul' : 1584,
    'Aug' : 3945,
    'Sep' : 4585,
    'Oct' : 3448,
    'Nov' : 3486,
    'Dec' : 2654,
}

total = sum(Elec_bill.values())

print(f"Total Electricity bills is {total}")
print(f"Average Electricity bills is {total/12}")