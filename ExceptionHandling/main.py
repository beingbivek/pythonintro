# Exception Handling
try:
    num1 = input("Enter Number 1: ")
    num2 = input("Enter Number 2: ")
    sum = float(num1) + float(num2)
    print(f"Total is {sum}")

except:
    print("Please enter all numeric value.")

finally:
    print("Back to Program")