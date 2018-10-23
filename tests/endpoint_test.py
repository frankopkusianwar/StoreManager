import json
import pytest
from backend.routes import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass 
    request.addfinalizer(teardown)
    return test_client

@pytest.fixture()
def data():
    data = {
        "productName": "kodak",
        "quantity": "60",
        "price": "500"
    }
    return data

@pytest.fixture()
def sales():
    data = {
        "atendantName": "john doe",
        "productName": "kodak",
        "quantity": "60",
        "unitPrice": "500"
    }
    return data

def test_postProducts(client, data):
    response = client.post('storemanager/admin/api/v1/products', data=json.dumps(data))
    assert response.status_code == 201