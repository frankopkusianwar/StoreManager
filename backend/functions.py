products = []
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

    
