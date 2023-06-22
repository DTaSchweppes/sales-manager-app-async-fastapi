from fastapi.testclient import TestClient
from fastapi import status
from app.main import app

# python -m pytest app/tests/

client = TestClient(app=app)

second_categ = "Строительный инструмент"


def test_create_main_category():
    response = client.post("/main_categories", json={"name": second_categ})
    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {
        "code": "201",
        "status": "Ok",
        "message": "Main category created successfully",
        "result": second_categ
    }


def test_get_main_category():  #
    response = client.get(f"/main_categories?name={second_categ}")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {"code": "200", "status": "Ok", "message": "Get item", "result": second_categ}


def test_create_vendor():
    response = client.post("/vendors", json={"name": "Дарси"})
    assert response.status_code == status.HTTP_201_CREATED


def test_create_brand():
    response = client.post("/brands", json={"name": "Зубр"})
    assert response.status_code == status.HTTP_201_CREATED


def test_create_second_category():
    response = client.post("/second_categories",
                           json={"name": "Расходные инструменты по бетону", "main_category_id": 1})
    assert response.status_code == status.HTTP_201_CREATED


def test_create_item():
    response = client.post("/items", json={"code": "012-3456", "name": "Зубило пикообразное 250 мм 29361-00-250",
                                           "image": "image.jpg", "category": 2, "vendor": 1, "brand": 1})
    assert response.status_code == status.HTTP_201_CREATED


def test_get_item():  #
    response = client.get("/items?id=1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "code": "200",
        "status": "Ok",
        "message": "Get item",
        "result": {
            "id": 1,
            "image": "image.jpg",
            "vendor": 1,
            "code": "012-3456",
            "name": "Зубило пикообразное 250 мм 29361-00-250",
            "category": 2,
            "brand": 1
        }
    }


def test_patch_item():  #
    response = client.patch("/items?id=1&name=saddsa&img=asddas")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "code": "200",
        "status": "Ok",
        "message": "Get item",
        "result": {
            "id": 2,
            "image": "asddas",
            "vendor": 1,
            "code": "012-3456",
            "name": "saddsa",
            "category": 2,
            "brand": 1
        }
    }


def test_delete_item():  #
    response = client.delete("/items?id=1")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {
        "code": "200",
        "status": "Ok",
        "message": "Get item",
        "result": {
            "id": 1,
            "image": "image.jpg",
            "vendor": 1,
            "code": "012-3456",
            "name": "Зубило пикообразное 250 мм 29361-00-250",
            "category": 2,
            "brand": 1
        }
    }
