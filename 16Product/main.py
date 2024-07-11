import os
from product import Product

askuseroption = """
Enter
'1' to Add New Product
'2' to Delete Product
'3' to Edit Product
'4' to View All Products
'5' to Search Product
'6' to Exit: 
"""

useroptionedit = """
'1' for ID
'2' for Product Name
'3' for Quantity
'4' for Price
or Press any other key to Cancel Update: 
"""


fileLocation = "./16Product/product.csv"
_isLoop = True

def readFile():
    dataobjlist = []
    f = open(fileLocation,'r')
    fileData = f.read().split("\n")
    f.close()
    nestList = [ data.split(",") for data in fileData ]
    for data in nestList:
        if data != ['']:
            p = Product(data[0],data[1],data[2],data[3])
            dataobjlist.append(p)
        else: pass
    return dataobjlist

def askID():
    return input("Enter the ID of the Product: ")

def writeFile(data):
    f = open(fileLocation,'a')
    f.write(data)
    f.close

def searchProduct():
    searchID = askID()
    for data in readFile():
        if searchID == data.getID():
            searchedData = data
            break
        else:
            searchedData = None
    return searchedData
    

def addData():
    user_input = int(input("Enter No. of products to add: "))
    # getID = [ data.getID() for data in readFile()]
    i=0
    while(user_input > i):
        print("\n")
        p = Product()
        p.id = input(f"Enter Product {i+1} ID: ")
        getID = [ data for data in readFile() if id == data.getID()]
        # print(getID)
        if getID == []:
            p.name = input(f"Enter Product {i+1} Name: ")
            p.quantity = input(f"Enter Product {i+1} Quantity: ")
            p.price = input(f"Enter Product {i+1} Price: ")
            i+=1
            writeFile(f"{p.id},{p.name},{p.quantity},{p.price}\n")
        else: print("Can't have same id for two products.")

def deleteData():
    delData = searchProduct()
    if delData != None:
        isSure = input(f"Are you sure you want to delete product {delData.name} (Y/N): ").lower()
        if isSure == 'y':
            finalData = [ data for data in readFile() if delData.id != data.getID()]
            # print(finalData)
            os.remove(fileLocation)
            for data in finalData: 
                writeFile(f"{data.id},{data.name},{data.quantity},{data.price}\n")
            print(f"{delData.name} has been deleted.")
        else: print(f"{delData.name} isn't deleted.")
    else: print("Can't Find Product to Delete.")

def editProduct(value,type,editedProduct):
    finalData = [ data for data in readFile() if editedProduct.id != data.getID() ]
    editedProduct.updateData(value,type)
    finalData.append(editedProduct)
    # print(finalData)
    os.remove(fileLocation)
    for data in finalData: 
        writeFile(f"{data.id},{data.name},{data.quantity},{data.price}\n")
    print(f"{editedProduct.id} is updated.")

def showProducts():
    print("ID\tProduct\t\tQuantity\tPrice\tTotal")
    for data in readFile():
        viewData = data.getAllData()
        print(f"{viewData[0]}\t{viewData[1]}\t\t{viewData[2]}\t{viewData[3]}\t{int(viewData[2])*int(viewData[3])}\n")

# try:
while _isLoop:
    value = int(input(askuseroption))
    if value == 1:
        addData()

    elif value == 2:
        deleteData()

    elif value == 3:
        editData = searchProduct()
        if editData != None:
            isType = input(f"What do you want to edit in this product {editData.getAllData()} {useroptionedit}")
            if isType == '1': value = input("Enter new ID: "); editProduct(value,isType,editData)
            elif isType == '2': value = input("Enter new Product Name: "); editProduct(value,isType,editData)
            elif isType == '3': value = input("Enter new Quantity: "); editProduct(value,isType,editData)
            elif isType == '4': value = input("Enter new Price: "); editProduct(value,isType,editData)
            else: print("Update is cancelled.")
        else: print("Can't Find Product to Edit.")
    
    elif value == 4:
        showProducts()

    elif value == 5:
        data = searchProduct()
        if data != None:
            print(data[0],data[1],data[2],data[3])
        else:
            print("Can't Find the product")
        
    elif value == 6:
        _isLoop = False

# except:
#     print("Invalid")