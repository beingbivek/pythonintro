# Create a program that calculates simple interest based on user input for principal, rate, and time.

print("Welcome, This program will calculate your simple interest.")
p = int(input("Enter Principal Amount: "))
r = int(input("Enter Rate: "))
t = int(input("Enter Time (in Yrs): "))

# Simple Interest
SI = (p*t*r)/100
print(f"Simple Interest is Rs.{SI}")