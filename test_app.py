import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add(client):
    response = client.get('/add?a=10&b=5')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 15.0

def test_subtract(client):
    response = client.get('/subtract?a=10&b=5')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 5.0

def test_multiply(client):
    response = client.get('/multiply?a=10&b=5')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 50.0

def test_divide(client):
    response = client.get('/divide?a=10&b=5')
    data = response.get_json()
    assert response.status_code == 200
    assert data['result'] == 2.0

def test_divide_zero(client):
    response = client.get('/divide?a=10&b=0')
    data = response.get_json()
    assert response.status_code == 400
    assert 'error' in data
    assert data['error'] == "Division by zero is not allowed."

def test_invalid_input(client):
    response = client.get('/add?a=abc&b=5')
    data = response.get_json()
    assert response.status_code == 400
    assert 'error' in data
    assert "Invalid input" in data['error']
