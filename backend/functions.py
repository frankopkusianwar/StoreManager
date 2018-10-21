products = []
sales = []

class Products(object):
    def __init__(self):
        pass
    def createProduct(self,productName,quantity,price):
        productItem = {
            "id": len(products)+1,
            "productName": productName,
            "quantity": quantity,
            "price": price
        }
        products.append(productItem)
        return products

    
class Sales:
    def __init__(self):
        pass

    def createSales(self, atendant, productName, quantity, unitPrice):
        subTotal = int(unitPrice) * int(quantity)
        records = {
            "id": len(sales)+1,
            "atendant": atendant,
            "product Name": productName,
            "quantity": quantity,
            "unit Price": unitPrice,
            "subTotal": str(subTotal) + "{}".format("ugx")

        }
        sales.append(records)
        return sales
