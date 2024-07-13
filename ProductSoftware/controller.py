import os
import filecrud as file
from product import Product


def searchProduct():
    searchID = input("Enter the ID of the Product: ")
    for data in file.readFile():
        if searchID == data.getID():
            searchedData = data
            break
        else:
            searchedData = None
    return searchedData
    

def addData():
    user_input = int(input("Enter No. of products to add: "))
    i=0
    while(user_input > i):
        print("\n")
        p = Product(id="",name="",quantity="",price="")
        p.id = input(f"Enter Product {i+1} ID: ")
        getID = [ data for data in file.readFile() if p.id == data.getID()]
        if getID == []:
            p.name = input(f"Enter Product {i+1} Name: ")
            p.quantity = input(f"Enter Product {i+1} Quantity: ")
            p.price = input(f"Enter Product {i+1} Price: ")
            i+=1
            file.writeFile(f"{p.id},{p.name},{p.quantity},{p.price}\n")
            print(f"{p.name} has been successfully added.")
        else: print("Can't have same id for two products.")

def deleteData():
    delData = searchProduct()
    if delData != None:
        isSure = input(f"Are you sure you want to delete product {delData.name} (Y/N): ").lower()
        if isSure == 'y':
            finalData = [ data for data in file.readFile() if delData.id != data.getID()]
            os.remove(file.fileLocation)
            for data in finalData: 
                file.writeFile(f"{data.id},{data.name},{data.quantity},{data.price}\n")
            print(f"{delData.name} has been deleted.")
        else: print(f"{delData.name} isn't deleted.")
    else: print("Can't Find Product to Delete.")

def editProduct(value,type,editedProduct):
    finalData = [ data for data in file.readFile() if editedProduct.id != data.getID() ]
    editedProduct.updateData(value,type)
    finalData.append(editedProduct)
    os.remove(file.fileLocation)
    for data in finalData: 
        file.writeFile(f"{data.id},{data.name},{data.quantity},{data.price}\n")
    print(f"{editedProduct.id} is updated.")

def showProducts():
    print("ID\tProduct\tQuantity\tPrice\tTotal")
    for data in file.readFile():
        data.displayData()
