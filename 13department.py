names = [
    # name, department
    ("Sagar Aryal", "Microbiology"),
    ("Santosh Adhikari", "IT"),
    ("Bivek Thapa", "Engineering"),
    ("Binod Rayamaje", "Microbiology"),
    ("Samyak Pokharel", "MBA"),
    ("Mandip Bista", "IT")
]

# Find all form microbiology depart
dept_mb = [dept for dept in names if dept[1].lower() == 'microbiology']
print(dept_mb)