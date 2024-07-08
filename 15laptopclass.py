# Write a python program to create a class Laptop with properties [id, name, ram] and create 3 objects of it and print all details.

class Laptop:
    def __init__(self, id, name, ram):
        self.id = id
        self.name = name
        self.ram = ram

    def display(self):
        print(f"ID no. {self.id} Laptop is {self.name} and has {self.ram} GB of RAM")

# How to create object

laptop1 = Laptop(id=1,name = "Acer Predator Triton 300 SE", ram=16)
laptop1.display()

laptop2 = Laptop(id=2,name = "Apple Macbook Air M1", ram=8)
laptop2.display()

laptop3 = Laptop(id=3,name = "Dell XPS 2023", ram=32)
laptop3.display()