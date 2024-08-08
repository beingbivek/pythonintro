import datetime
from dateutil import relativedelta

print("Enter details for Date 1:")
year1 = int(input("Enter Year: "))
month1 = int(input("Enter Month: "))
day1 = int(input("Enter Day: "))
print("Enter details for Date 2:")
year2 = int(input("Enter Year: "))
month2 = int(input("Enter Month: "))
day2 = int(input("Enter Day: "))
date1 = datetime.date(year1,month1,day1)
date2 = datetime.date(year2,month2,day2)
delta = relativedelta.relativedelta(date2, date1)
print('Years, Months, Days between two dates is')
print(delta.years, 'Years,', delta.months, 'months,', delta.days, 'days')