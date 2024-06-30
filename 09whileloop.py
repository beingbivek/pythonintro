# While loop

atm_pin = '1456'
user_pin = ''
attempt = 0

while atm_pin != user_pin:
    if attempt > 0:
        print(f"Invalid pin code. Total Attempt {attempt}")
    user_pin = input("Enter ATM Pin: ")
    attempt += 1

print("Access Granted, How much you want to withdraw?")

