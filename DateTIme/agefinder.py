import datetime

try:
    birth_year = int(input("Enter birth Year: "))
    today_year = datetime.date.today().year
    print(f"age is {today_year-birth_year}")
except:
    print("Use Numbers for year")
finally:
    print("Rerun Program")