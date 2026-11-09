def test_response():
    response = {
        "status": 201,
        "user": {"name": "Ivan", "role": "tester"},
        "tags": ["qa", "python"]
    }
    assert response["status"] == 201
    assert response["user"]["role"] == "tester"
    assert response["tags"][0] == "qa"

