class Student:
    def __init__(self, name, phone) -> None:
        self.name = name
        self.phone = phone

    def display(self):
        print(f"Name is {self.name} and phone is {self.phone}")