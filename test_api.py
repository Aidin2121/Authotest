import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"
@pytest.mark.smoke
def test_get_user():
    response = requests.get(f"{BASE_URL}/users/1")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == 1
    assert data["address"]["city"] == "Gwenborough"

@pytest.mark.smoke
def test_get_nonexistent_user():
    response = requests.get(f"{BASE_URL}/users/9999")
    assert response.status_code == 404


@pytest.mark.parametrize("user_id", [1, 2, 3, 4, 5])
def test_user_exists(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    data = response.json()
    assert response.status_code == 200
    assert data["id"] == user_id


@pytest.mark.parametrize("user_id, expected_status", [
        (1, 200),
        (9999, 404),
        (10, 200),
        (0, 404)
    ])
def test_user_status(user_id, expected_status):
        response = requests.get(f"{BASE_URL}/users/{user_id}")
        assert response.status_code == expected_status