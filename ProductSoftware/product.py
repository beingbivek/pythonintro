class Product:
    def __init__(self,id,name,quantity,price) -> None:
        self.id = id
        self.name = name
        self.quantity = quantity
        self.price = price

    def getID(self):
        return self.id
    
    def getAllData(self):
        productDetails = [self.id,self.name,self.quantity,self.price]
        return productDetails
    
    def updateData(self,value,type):
        if type == '1': self.id = value
        elif type == '2': self.name = value
        elif type == '3': self.quantity = value
        elif type == '4': self.price = value
        else: pass

    def displayData(self):
        print(self.id,"\t",self.name,"\t",self.quantity,"\t",self.price,int(self.quantity)*int(self.price))