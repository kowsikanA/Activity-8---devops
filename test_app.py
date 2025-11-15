from app import app


def client():
    return app.test_client()


def test_hello():
    resp = client().get("/hello")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": "Hello, World!"}


def test_echo():
    payload = {"foo": "bar", "n": 3}
    resp = client().post("/echo", json=payload)
    assert resp.status_code == 201
    assert resp.get_json() == payload


def test_message_get_initial():
    # Should be empty at start of test run
    resp = client().get("/message")
    assert resp.status_code == 200
    assert resp.get_json() == {"message": ""}


def test_message_put_and_get():
    put_payload = {"message": "Hi there"}
    put_resp = client().put("/message", json=put_payload)
    assert put_resp.status_code == 200
    assert put_resp.get_json() == {"message": "Hi there"}

    get_resp = client().get("/message")
    assert get_resp.status_code == 200
    assert get_resp.get_json() == {"message": "Hi there"}


def test_message_delete():
    # Set something first
    client().put("/message", json={"message": "temp"})
    del_resp = client().delete("/message")
    assert del_resp.status_code == 200
    assert del_resp.get_json() == {"deleted": True, "message": ""}

    # Verify cleared
    get_resp = client().get("/message")
    assert get_resp.status_code == 200
    assert get_resp.get_json() == {"message": ""}
