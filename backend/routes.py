from flask import Flask, jsonify, request, make_response, abort
from functions import Products
from functions import products


app = Flask(__name__)

@app.route('/storemanager/admin/api/v1/products', methods=['POST'])
def postProduct():
    json_data = request.get_json(force=True)
    prod = Products()
    prod.createProduct(json_data['productName'],
                           json_data['quantity'], 
                           json_data['price'])
    return make_response(jsonify({'message': "product created"}), 201)

@app.route('/storemanager/api/v1/products', methods=['GET'])
def getProduct():
    if len(products) == 0:
        abort(404)
    return make_response(jsonify({'products':products},200))
@app.errorhandler(404)

@app.route('/storemanager/api/v1/products/<int:productId>', methods=['GET'])
def getSpecificProduct(productId):
    prod = [prod for prod in products if prod['id'] == productId]
    if len(products) == 0:
        abort(404)
    return make_response(jsonify({'product':prod[0]},200))

def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)