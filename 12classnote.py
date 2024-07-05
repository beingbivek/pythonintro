# def age_finder(dob):
#     age = 2024 - dob
#     print(f"Age is {age}")

# def test_funciton():
#     pass # used to pass this function

# age_finder(1997)

# # Scope - area of the functions
# def displayName():
#     name = 'bivek thapa'
#     print(name)

# displayName() 

# WAP to reverse string
def rev_str(n):
    rstr = ""
    for c in n:
        rstr = c + rstr

    return rstr

# or we can use range
# for i in range(len(n),-1,-1):
#     rstr = rstr + n[i]

name = input("Enter your name: ")
print(f"Your name is {name} and it's reverse is {rev_str(name)}")