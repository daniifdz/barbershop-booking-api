from sqlalchemy import select

from app.models import User


VALID_USER = {
    "email": "Prueba@Mail.com",
    "password": "hola1234",
    "full_name": "Usuario Prueba",
    "phone": "600000000",
}


def test_register_creates_user(client):
    response = client.post("/auth/register", json=VALID_USER)

    assert response.status_code == 201
    body = response.json()
    assert body["email"] == "prueba@mail.com"
    assert body["role"] == "client"
    assert "password" not in body
    assert "password_hash" not in body
    
    
def test_register_rejects_duplicate_email(client):
    first = client.post("/auth/register", json=VALID_USER)
    second = client.post("/auth/register", json=VALID_USER)

    assert first.status_code == 201
    assert second.status_code == 409


def test_register_rejects_same_email_with_different_case(client):
    client.post("/auth/register", json=VALID_USER)
    other_case = {**VALID_USER, "email": "prueba@mail.com"}

    response = client.post("/auth/register", json=other_case)

    assert response.status_code == 409


def test_register_stores_hashed_password(client, db_session):
    client.post("/auth/register", json=VALID_USER)

    user = db_session.scalar(select(User))

    assert user.password_hash != VALID_USER["password"]
    assert user.password_hash.startswith("$argon2")