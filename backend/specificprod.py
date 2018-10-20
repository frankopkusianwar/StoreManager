from flask import Flask, jsonify, request, make_response, abort
from functions import products

app = Flask(__name__)

@app.route('/storemanager/api/v1/products<int:productId>', methods=['GET'])
def getProduct(productId):
    prod = [prod for prod in products if prod['id'] == productId]
    if len(products) == 0:
        abort(404)
    return make_response(jsonify({'product':prod[0]},200))
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)