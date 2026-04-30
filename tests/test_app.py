import pytest
from fastapi.testclient import TestClient
from webapp.app import app

client = TestClient(app)

# 1. Integration Test: Normal valid input
def test_predict_normal_input():
    response = client.post("/predict", json={"text": "I really love this framework!"})
    assert response.status_code == 200
    assert "sentiment" in response.json()

# 2. Edge Case Test: Empty string input
def test_predict_empty_text():
    response = client.post("/predict", json={"text": "   "})
    assert response.status_code == 400
    assert response.json()["detail"] == "Text cannot be empty"

# 3. Stress Test: Extremely long text input
def test_predict_long_text():
    long_text = "excellent " * 500
    response = client.post("/predict", json={"text": long_text})
    assert response.status_code == 200
    assert "sentiment" in response.json()

# 4. Robustness Test: Invalid input format (missing required field)
def test_predict_invalid_json():
    response = client.post("/predict", json={"wrong_key": "This should fail"})
    assert response.status_code == 422 # FastAPI default status for validation errors