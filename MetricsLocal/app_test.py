import pytest
from flask import json
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_page(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert rv.data == b'Welcome to MetricsLocal!'

def test_process_request(client):
    rv = client.get('/i', query_string={
        "app_key": "test_app_key",
        "timestamp": "test_timestamp",
        "hour": "test_hour",
        "dow": "test_dow",
        "tz": "test_tz",
        "sdk_version": "test_sdk_version",
        "sdk_name": "test_sdk_name",
        "user_details": "test_user_details",
        "device_id": "test_device_id",
        "checksum": "test_checksum"
    })
    assert rv.status_code == 200
    json_data = json.loads(rv.data)
    assert json_data["app_key"] == "test_app_key"
    # ... add other assertions as needed