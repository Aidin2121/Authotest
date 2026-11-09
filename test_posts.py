import requests
import pytest





@pytest.fixture
def created_post(api_base_url):
    payload = {
        "title": "My first post",
         "body": "QA is fun",
         "userId": 1
    }

    response = requests.post(f"{api_base_url}/posts", json=payload)
    return response


def test_post_status(created_post):
    assert created_post.status_code == 201


def test_post_title(created_post):
    data = created_post.json()
    assert data["title"] == "My first post"

def test_post_user_id(created_post):
    data = created_post.json()
    assert data["userId"] == 1
