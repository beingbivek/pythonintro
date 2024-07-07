# List Comprehension

# Even Numbers
numbers = [1,2,3,4,5,6,7,8,9]

even_num = [x for x in numbers if x % 2 == 0]

print(even_num)

# String

names = ['Bivek','America','Africa','Random','Oli','Bijulidai']

# Find all names starts with A

starts_a = [name for name in names if name[0].lower() == 'a']
# OR
start_with_a = [name for name in names if name.startswith("A")]

print(starts_a)
print(start_with_a)
