import importlib

import pytest


@pytest.fixture()
def client(tmp_path, monkeypatch):
    monkeypatch.setenv("DATA_DIR", str(tmp_path))
    monkeypatch.setenv("APP_GREETING", "Hello")
    import app as app_module

    importlib.reload(app_module)
    return app_module.app.test_client()


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.get_json() == {"status": "ok"}


def test_greet_default(client):
    assert client.get("/greet").get_json() == {"message": "Hello, world!"}


def test_greet_name(client):
    assert client.get("/greet?name=Ada").get_json() == {"message": "Hello, Ada!"}


def test_visit_counts_up(client):
    assert client.get("/visit").get_json() == {"visits": 1}
    assert client.get("/visit").get_json() == {"visits": 2}


def test_info(client):
    r = client.get("/info")
    assert r.status_code == 200
    assert r.get_json() == {
        "app": "ceng413-hw1",
        "version": "1.0",
        "framework": "Flask",
    }


def test_motivation(client):
    r = client.get("/motivation")
    assert r.status_code == 200

    data = r.get_json()
    assert "message" in data
    assert isinstance(data["message"], str)
    assert len(data["message"]) > 0
