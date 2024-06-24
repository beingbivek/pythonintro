# Write a script that calculates Body Mass Index (BMI) from user input (height and weight) using variables, data types, and operators.

print("Welcome to Body Mass Index (BMI) Calculator")
height = int(input("Enter Your Height in cm: "))
weight = int(input("Enter Your Weight in Kg: "))

BMI = (weight/((height/100)**2))

print(f"Your BMI is {BMI}")