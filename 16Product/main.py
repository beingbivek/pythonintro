import os
from product import Product

askusertext = "\nEnter\n'1' to Add New Product\n'2' to Delete Product\n'3' to Edit Product\n'4' to View All Products\n'5' to Search Product\n'6' to Exit\n: "
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
            searchedData = data.getAllData()
            break
        else:
            searchedData = []
    return searchedData
    

def addData():
    user_input = int(input("Enter No. of products to add: "))
    # getID = [ data.getID() for data in readFile()]
    i=0
    while(user_input > i):
        print("\n")
        id = input(f"Enter Product {i+1} ID: ")
        getID = [ data for data in readFile() if id == data.getID()]
        # print(getID)
        if getID == []:
            n = input(f"Enter Product {i+1} Name: ")
            q = input(f"Enter Product {i+1} Quantity: ")
            p = input(f"Enter Product {i+1} Price: ")
            i+=1
            writeFile(f"{id},{n},{q},{p}\n")
        else: print("Can't have same id for two products.")

def deleteData():
    delID = askID()
    delData = [ data for data in readFile() if delID == data.getID()]
    isSure = input(f"Are you sure you want to delete product {delData[0].getAllData()} (Y/N): ").lower()
    if isSure == 'y':
        finalData = [ data for data in readFile() if delID != data.getID()]
        # print(finalData)
        os.remove(fileLocation)
        for data in finalData: 
            writeFile(f"{data.id},{data.name},{data.quantity},{data.price}\n")
        print(f"{delData[0].name} has been deleted.")
    else: print(f"{delData[0].name} isn't deleted.")

def editProduct(value,type,editedProduct):
    finalData = [ data for data in readFile() if editedProduct[0].id != data.getID() ]
    editedProduct[0].updateData(value,type)
    finalData.append(editedProduct[0])
    # print(finalData)
    os.remove(fileLocation)
    for data in finalData: 
        writeFile(f"{data.id},{data.name},{data.quantity},{data.price}\n")
    print(f"{editedProduct[0].id} is updated.")

def showProducts():
    print("ID\tProduct\t\tQuantity\tPrice\tTotal")
    for data in readFile():
        viewData = data.getAllData()
        print(f"{viewData[0]}\t{viewData[1]}\t\t{viewData[2]}\t{viewData[3]}\t{int(viewData[2])*int(viewData[3])}\n")

# try:
while _isLoop:
    value = int(input(askusertext))
    if value == 1:
        addData()

    elif value == 2:
        deleteData()

    elif value == 3:
        editID = askID()
        editData = [data for data in readFile() if editID == data.getID()]
        isType = input(f"What do you want to edit in this product {editData[0].getAllData()}:\n'1' for ID\n'2' for Product Name\n'3' for Quantity\n'4' for Price\nor Press any other key to Cancel Update\n: ")
        if isType == '1': value = input("Enter new ID: "); editProduct(value,isType,editData)
        elif isType == '2': value = input("Enter new Product Name: "); editProduct(value,isType,editData)
        elif isType == '3': value = input("Enter new Quantity: "); editProduct(value,isType,editData)
        elif isType == '4': value = input("Enter new Price: "); editProduct(value,isType,editData)
        else: print("Update is cancelled.")
    
    elif value == 4:
        showProducts()

    elif value == 5:
        data = searchProduct()
        if data != []:
            print(data[0],data[1],data[2],data[3])
        else:
            print("Can't Find the product")
        
    elif value == 6:
        _isLoop = False

# except:
#     print("Invalid")