from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_risk():
    response = client.post("/risks/", json={"title": "Teste", "description": "Descrição do teste"})
    assert response.status_code == 200
    assert response.json()["title"] == "Teste"

def test_get_risk():
    response = client.get("/risks/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1
