# OOP - Object Oriented Programming, In OOP we user class and object to design computer programs.

# Class: Blueprint to Create Object
# Object: Instance of Class

# Create class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")

# How to create object

st1 = Student(name = "Ajaya", age=30)
st1.display()

st2 = Student(name = "Ram", age=24)
st2.display()

# Create  class teacher with parameter name and salary and display method
# Create 3 objects and display them

# class Teacher:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display(self):
#         print(f"Name is {self.name}")
#         print(f"Salary is {self.salary}")


# t1 = Teacher(name = "Bivek", salary=30000)
# t1.display()

# t2 = Teacher(name = "Bivansh", salary=24000)
# t2.display()

# t3 = Teacher(name = "Arati", salary=25000)
# t3.display()

class Teacher:
    def __init__(self, teacherName, subject, address):
        self.teacherName = teacherName
        self.subject = subject
        self.address =  address
    
    def display(self):
        print(f"Teacher Name is : {self.teacherName}\t Subject : {self.subject}")

teacher1 = Teacher(teacherName="Ram Karki", subject= "Science", address="Bkt")
teacher3 = Teacher(teacherName="Hritesh Karki", subject= "Social", address="Banepa")
teacher2 = Teacher(teacherName="Ramita Karki", subject= "Nepali", address="Ktm")
teacher4 = Teacher(teacherName="Ramgopal Shrestha", subject= "Math", address="Lalitpur")
teacher5 = Teacher(teacherName="Shyam Kc", subject= "English", address="Naikap")

teacher1.display()
teacher3.display()
teacher2.display()
teacher4.display()
teacher5.display()