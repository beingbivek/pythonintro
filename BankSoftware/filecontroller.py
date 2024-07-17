from customer import Customer
import csv

filelocation = './BankSoftware/customer.csv'

def convert_list_to_csv(listofcustomers):
    f = open(filelocation,'a')
    for c in listofcustomers:
        f.write(f"{c.i},{c.n},{c.p},{c.b},{c.c}\n")
    f.close()

# def convert_csv_to_list(): # This is also a right way
#     f = open(filelocation,'r')
#     fileData = f.read().splitlines()
#     f.close()
#     return fileData

def convert_csv_to_list(): # This is efficient way using Class and CSV
    all_customer = []
    with open(filelocation,'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            # print(row)
            customer = Customer(id=row[0],name=row[1],phone=row[2],balance=row[3],ctzno=row[4])
            all_customer.append(customer)
    # print(all_customer)
    return all_customer