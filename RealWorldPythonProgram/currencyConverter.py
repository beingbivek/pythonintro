# Create a basic currency converter that takes user input for the amount and converts it between predefined currencies (e.g., USD to EUR).

amount = int(input("Enter Amount: "))
print("Select the currency for the Amount.")
selected = int(input("Enter 1 for USD, 2 for Euro, 3 for NPR and 4 for AUD: "))

if selected == 1:
    print(f"${amount} is equal to {amount*0.93} Euro, {amount*133.64} NPR and {amount * 1.51} AUD")
elif selected == 2:
    print(f"{amount} Euro is equal to ${amount*1.07} USD, {amount*143.40} NPR and {amount * 1.62} AUD")
elif selected == 3:
    print(f"Rs.{amount} NPR is equal to ${amount * 0.0075} USD, {amount * 0.007} Euro and {amount * 0.01} AUD")
elif selected == 4:
    print(f"{amount} AUD is equal to ${amount * 0.66} USD, {amount*88.75} NPR and {amount * 0.62} Euro")
else:
    print("Selected Number isnot assigned, Run the program again.")