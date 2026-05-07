from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World API is running"}


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_process_text_endpoint():
    response = client.post(
        "/process-text",
        json={"text": "Ahoj z testu"}
    )

    assert response.status_code == 200
    assert response.json() == {
        "message": "Přijal jsem text: Ahoj z testu",
        "length": 12
    }


def test_classify_text_invoice():
    response = client.post(
        "/classify-text",
        json={"text": "Dobrý den, v příloze zasíláme fakturu."}
    )

    assert response.status_code == 200
    assert response.json()["is_invoice"] is True


def test_classify_text_not_invoice():
    response = client.post(
        "/classify-text",
        json={"text": "Dobrý den, posílám informaci ke schůzce."}
    )

    assert response.status_code == 200
    assert response.json()["is_invoice"] is False