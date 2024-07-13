import controller as c

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

_isLoop = True

# try:
while _isLoop:
    value = int(input(askuseroption))
    if value == 1:
        c.addData()

    elif value == 2:
        c.deleteData()

    elif value == 3:
        editData = c.searchProduct()
        if editData != None:
            isType = input(f"What do you want to edit in this product {editData.getAllData()} {useroptionedit}")
            if isType == '1': value = input("Enter new ID: "); c.editProduct(value,isType,editData)
            elif isType == '2': value = input("Enter new Product Name: "); c.editProduct(value,isType,editData)
            elif isType == '3': value = input("Enter new Quantity: "); c.editProduct(value,isType,editData)
            elif isType == '4': value = input("Enter new Price: "); c.editProduct(value,isType,editData)
            else: print("Update is cancelled.")
        else: print("Can't Find Product to Edit.")
    
    elif value == 4:
        c.showProducts()

    elif value == 5:
        data = c.searchProduct()
        if data != None:
            data.displayData()
        else:
            print("Can't Find the product")
        
    elif value == 6:
        _isLoop = False

# except:
#     print("Invalid")