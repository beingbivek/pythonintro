# Develop a script that converts distances between kilometers, miles, and meters based on user input.
distance = int(input("Enter Distance: "))
print("Select the unit for the distance.")
selected = int(input("Enter 1 for Kilometer, 2 for Miles, 3 for Meter and 4 for Feet: "))

if selected == 1:
    print(f"{distance} Km is equal to {distance/1.6} miles, {distance*1000} meters and {distance * 3280.8399} feets")
elif selected == 2:
    print(f"{distance} miles is equal to {distance*1.6} Km, {distance*1609} meters and {distance * 5280} feets")
elif selected == 3:
    print(f"{distance} m is equal to {distance * 0.0006213712} miles, {distance/1000} Kilometers and {distance * 3.28084} feets")
elif selected == 4:
    print(f"{distance} feet is equal to {distance * 0.0001893939} miles, {distance*0.0003048} Kilometers and {distance * 0.3048} meters")
else:
    print("Selected Number isnot assigned, Run the program again.")