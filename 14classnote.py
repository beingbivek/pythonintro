# Make List with ['first','second','third']
names = ['Anish', 'Binod', 'Ratna']
# mixedlist = [1, "Bivek", 50, 14.4]

# Add Items in list
names.append("Bivek")
names.append("Bivek")
names.append("Bivek")
names.append("Saimon")

# Delete last item in list
# names.pop()
# Delete 3rd item in list
names.pop(3)

# Find total number of occurrences
total_bivek = names.count("Bivek")
print(total_bivek)

# Clear or remove everything from List
# names.clear()

# Index
# print(names[3])

# Sort in Ascending order
names.sort()

# To reverse list
# 1st sort and then
names.reverse()

# print(type(names))
# print(type(mixedlist))

for name in names:
    print(name)