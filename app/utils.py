from flask import jsonify

def getProducts(data):
    return jsonify(data)

def search(searchItem, data):
    searchedItem = []
    for item in data:
        [searchedItem.append(item) for key in item if item[key] == searchItem]
    return jsonify(searchedItem)