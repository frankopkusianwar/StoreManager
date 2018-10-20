from flask import Flask, jsonify, request, make_response
from functions import Products

app = Flask(__name__)

@app.route('/storemanager/admin/api/v1/products', methods=['POST'])
def postProduct():
    json_data = request.get_json(force=True)
    prod = Products()
    prod.createProduct(json_data['productName'],
                           json_data['quantity'], 
                           json_data['price'])
    return make_response(jsonify({'message': "product created"}), 201)

if __name__ == '__main__':
    app.run(debug=True)