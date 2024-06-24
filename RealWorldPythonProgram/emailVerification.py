# Create a program that formats a user-provided email address into different parts (username, domain) and validates its structure.

email = input("Enter Your email id: ")

try:
    splitemail = email.split("@")
    username = splitemail[0]
    domain = splitemail[1]
    try:
        s_domain = domain.split(".")
        print(f"Your username is {username} and domain is {s_domain[0]}.{s_domain[1]}")
    except: 
        print("Invalid Domain in Email ID")

except:
    print("Invalid Email ID")

