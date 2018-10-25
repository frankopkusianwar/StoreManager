from flask import json
import pytest
from routes import *

@pytest.fixture(scope="module")
def client():
    test_client = app.test_client()
    return test_client


@pytest.fixture()
def product():
    productData = {
        "productName": "kodak max",
        "quantity": "200",
        "price": "40000"
    }
    return productData

@pytest.fixture()
def sale():
    saleData = {
        "atendant": "frank",
        "product": "kodak",
        "quantity": "10",
        "unitPrice": "200"
    }
    return saleData


def test_post_product(client, data):
    respons = client.post('/storemanager/admin/api/v1/products', data=json.dumps(productData))
    assert respons.status_code == 201


def test_get_products(client):
    respons = client.get('/storemanager/api/v1/products')
    assert respons.status_code == 200

def test_post_sales(client, salesData):
    response = client.post('/storemanager/atendant/api/v1/sales', data=json.dumps(saleData))
    assert response.status_code == 201
