# Program to calculate total expenses and average expenses of a week

sunday_exp = 5411
monday_exp = 503
tuesday_exp = 956
wednesday_exp = 2154
thursday_exp = 966
friday_exp = 1254
saturday_exp = 60

print(f"Expenses on sunday is {sunday_exp}")
print(f"Expenses on monday is {monday_exp}")
print(f"Expenses on tuesday is {tuesday_exp}")
print(f"Expenses on wednesday is {wednesday_exp}")
print(f"Expenses on thursday is {thursday_exp}")
print(f"Expenses on friday is {friday_exp}")
print(f"Expenses on saturday is {saturday_exp}")

total_exp = sunday_exp + monday_exp + tuesday_exp + wednesday_exp + thursday_exp + friday_exp + saturday_exp
avg_exp = total_exp / 7

print(f"Total Expenses is {total_exp}")
print(f"Average Expenses is {avg_exp}")