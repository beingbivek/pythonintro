# Develop a basic calculator that performs addition, subtraction, multiplication, and division based on user input.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
selected = int(input("Enter 1 to Add, 2 to Substract, 3 to Multiply and 4 to Division: "))

if selected == 1:
    print(f"Sum : {num1 + num2}")
elif selected == 2:
    print(f"Subtraction : {num1 - num2}")
elif selected == 3:
    print(f"Multiplication : {num1 * num2}")
elif selected == 4:
    print(f"Division : {num1 / num2}")
else:
    print("Selected Number isnot assigned, Run the program again.")