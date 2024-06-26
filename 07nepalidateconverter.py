# Create Software that convert English Date to Nepali Date

import datetime
import nepali_datetime

print("Date Conversion Software")
selected = int(input("Enter 1 for BS to AD and 2 for AD to BS Conversion: "))

if selected == 1:
    nep_date = input("Enter Nepali date in YYYY/MM/DD format: ")
    split_date = nep_date.split("/")
    eng_date = nepali_datetime.date(int(split_date[0]),int(split_date[1]),int(split_date[2])).to_datetime_date()
    print(f"Converted English date (AD) is {eng_date}")

elif selected == 2:
    eng_date = input("Enter English date in YYYY/MM/DD format: ")
    split_date = eng_date.split("/")

    nep_date = nepali_datetime.date.from_datetime_date(datetime.date(int(split_date[0]), int(split_date[1]), int(split_date[2])))

    print(f"Converted Nepali date is {nep_date}")

else:
    print("Incorrect Input, Please Run the program again")



