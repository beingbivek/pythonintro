# Create a program that converts temperatures between Celsius, Fahrenheit, and Kelvin using basic input and output, variables, and operators.

temptype = input("Type C for celcius, F for Fahrenheit and K for kelvin: ")

# F_value = tempvalue * 1.8 + 32 # Celsius to Fahrenheit Formula
# C_value = (tempvalue - 32) * (5/9) # Fahrenheit to Celsius Formula
# K_value = C_value + 273.15 # Celsius to Kelvin Formula

if temptype == "c" or temptype == "C":
    tempvalue = int(input("Enter Celsius Temperature: "))
    F_value = tempvalue * 1.8 + 32
    K_value = tempvalue + 273.15
    print(f"For {tempvalue}℃\nFahrenheit\t:\t{F_value}\nKelvin\t:\t{K_value}")
elif temptype == "f" or temptype == "F":
    tempvalue = int(input("Enter Fahrenheit Temperature: "))
    C_value = (tempvalue - 32) * (5/9)
    K_value = C_value + 273.15
    print(f"For {tempvalue}℉\nCelsius\t:\t{C_value}\nKelvin\t:\t{K_value}")
elif temptype == "k" or temptype == "K":
    tempvalue = int(input("Enter Kelvin Temperature: "))
    C_value = tempvalue - 273.15
    F_value = C_value * 1.8 + 32
    print(f"For {tempvalue}K\nCelsius\t:\t{C_value}\nFahrenheit\t:\t{F_value}")
else:
    print("Invalid Temperature Metric, Run the program again, Thank You")
    
   