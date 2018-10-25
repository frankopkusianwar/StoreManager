products = []
sales = []
import uuid
identifier = uuid.uuid4()
def createProduct(productName,quantity,price):
    productItem = {
        "id":len(products)+1,
        "productName": productName,
        "quantity": quantity,
        "price": price
    }  
    products.append(productItem)
    return products

def createSales(atendant, productName, quantity, unitPrice):
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