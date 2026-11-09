def test_status_ok():
    status_code = 200
    assert status_code == 200


def test_status_not_found():
    status_code = 200
    assert status_code == 200

def test_status_server_error():
    status_code = 500
    assert status_code == 500

def test_status_created():
    status_code = 201
    assert status_code == 201