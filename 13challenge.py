# create 10 employee who works in different department
# print all employee who are in IT department
# option:
# Display all dept along with their names.

names = [
    # name, department
    ("Sagar Aryal", "Engineering"),
    ("Santosh Adhikari", "IT"),
    ("Bivek Thapa", "Engineering"),
    ("Binod Rayamaje", "Designer"),
    ("Samyak Pokharel", "Account"),
    ("Mandip Bista", "IT"),
    ("Swopnil Khadka", "IT"),
    ("Bibek Koirala", "IT"),
    ("Sagar Dhakal", "Account"),
    ("Balen Shah", "Social Media"),
    ("Routiney", "Designer"),
    ("Mina Bista", "IT")
]

# print(names[0][0])

dept_names = {dept[1] for dept in names} # Set of Department Names
# print(dept_names)

for dept in dept_names:
    print("\n----------------\n")  
    print(f"{dept} Department") 
    print("\n") 
    for name in names:
        if name[1] == dept:
            print(name[0])

# Find all form all departments
dept_it = [dept[0] for dept in names if dept[1].lower() == 'it']
# dept_en = [dept[0] for dept in names if dept[1].lower() == 'engineering']
# dept_de = [dept[0] for dept in names if dept[1].lower() == 'designer']
# dept_ac = [dept[0] for dept in names if dept[1].lower() == 'account']
# dept_sm = [dept[0] for dept in names if dept[1].lower() == 'social media']


print("\nList of Employees in IT Departments\n")  
for dept in dept_it:
    print(dept)  
