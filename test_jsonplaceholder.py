# test_api.py
import requests

BASE_URL_POSTS = "https://jsonplaceholder.typicode.com/posts"
BASE_URL_USERS = "https://jsonplaceholder.typicode.com/users"

# Section A: POSTS API Tests

def test_get_posts():
    response = requests.get(BASE_URL_POSTS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_update_post():
    updated_data = {
        "id": 1,
        "title": "Updated Title",
        "body": "This post has been updated.",
        "userId": 1
    }
    response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=updated_data)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == updated_data["title"]
    assert data["body"] == updated_data["body"]
    assert data["id"] == 1


# Section B: USERS API Tests

def test_get_users():
    response = requests.get(BASE_URL_USERS)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_get_single_user():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "username" in data

def test_user_has_address():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    assert response.status_code == 200
    data = response.json()
    assert "address" in data
    assert "city" in data["address"]
