from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

#pytest solo ejecuta archivos y funciones que empiezan por test_
def test_health_returns_ok():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}