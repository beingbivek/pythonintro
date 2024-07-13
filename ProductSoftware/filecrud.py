from product import Product

fileLocation = "./ProductSoftware/product.csv"

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

def writeFile(data):
    f = open(fileLocation,'a')
    f.write(data)
    f.close