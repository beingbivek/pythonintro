resultset = {
    '0041144N': '4',
    '0023232A': '2',
    '0023833C': '3',
    '0023432V': '3.5',
}

symbol_no = input("Enter your symbol number: ")

result = ""
for i in resultset.keys():
    if symbol_no == i:
        result = resultset[i]
        break
    else:
        result = '' 

if result != "":
    print(f"Your result is {result}")
else:
    print("Your symbol number not found.")    