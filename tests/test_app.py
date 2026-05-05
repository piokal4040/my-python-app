from src.app import add, app


def test_add():
    assert add(2, 3) == 5


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["status"] == "running"


def test_add_numbers():
    client = app.test_client()

    response = client.get("/add/2/3")

    assert response.status_code == 200
    assert response.get_json()["result"] == 5
