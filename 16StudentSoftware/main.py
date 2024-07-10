from student import Student

f = open('./16StudentSoftware/contact.csv','a')

total_sts = int(input("Enter no. of student to save details: "))

for i in range(total_sts):
    n = input(f"Enter Student {i+1} name: ")
    p = input(f"Enter Student {i+1} phone: ")
    s = Student(name=n,phone=p)
    f.write(f"{s.name},{s.phone}\n")
f.close()

f = open('./16StudentSoftware/contact.csv','r')
data = f.read()
print(data)