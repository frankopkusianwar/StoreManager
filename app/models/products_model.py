import uuid

class Product:
    productName = ""
    def __init__(self, quantity=0, price=0.00, id= str (uuid.uuid4())):
        self.quantity = quantity
        self.price = price
        self.id = id

productList = [
{
    "id": str(uuid.uuid4()),
    "productName": "kodak max", 
    "quantity": 30,
    "price": 100000
},
{
    
    "id": str(uuid.uuid4()),
    "productName": 'kodak max', 
    "quantity": 30,
    "price": 100000
},
]