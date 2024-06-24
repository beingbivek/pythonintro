# Write a program that calculates a user's age based on their birth year.

from datetime import datetime

birthyear = int(input("Your Year of Birth: "))
y = datetime.now()

print(f"Your Age is {y.year - birthyear}.")