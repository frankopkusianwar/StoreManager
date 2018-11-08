from flask import Blueprint, request, Response
from app.models.products_model import Product, productList
from app.utils import getProducts,search

bp = Blueprint("productsView", __name__, url_prefix="/api/v1")

@bp.route("admin/products", methods=["POST"])
def postProduct():
    product = Product()
    request_data = request.get_json()
    product.productName = request_data["productName"]
    product.quantity = request_data["quantity"]
    product.price = request_data["price"]
    productData = {
        "id": product.id,
        "product Name": product.productName,
        "quantity": product.quantity,
        "price": product.price
    }
    productList.append(productData)
    return Response("Product %s created successfully" % product.productName, status=201)

@bp.route("/products", methods= ["GET"])
def getAllProducts():
    return getProducts(productList)

@bp.route("/products/<id>")
def getSingleProduct(id):
    if len(productList) > 0:
        return  search(id, productList)