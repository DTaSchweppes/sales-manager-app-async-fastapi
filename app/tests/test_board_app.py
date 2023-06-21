from fastapi.testclient import TestClient
from fastapi import status
from main import app
#python -m pytest app/tests/

client = TestClient(app=app)


def test_create_main_category():
    response = client.post("/main_categories", json={"name": "Насосы"})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
  "code": "201",
  "status": "Ok",
  "message": "Main category created successfully",
  "result": "Насосы"
}
