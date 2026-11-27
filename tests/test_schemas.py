import pytest
from pydantic import ValidationError

from app.schemas.user import UserCreate


def test_user_create_accepts_valid_data():
    user = UserCreate(email="hola123@gmail.com",
                      password="hola1234",
                      full_name="Nombre Completo",
                      phone="123456789")
    
    assert user.email == "hola123@gmail.com"
    assert user.password == "hola1234"
    assert user.full_name == "Nombre Completo"
    assert user.phone == "123456789"
    
def test_user_create_rejects_short_password():
    with pytest.raises(ValidationError):
        UserCreate(
            email="hola123@gmail.com",
            password="hola",
            full_name="Nombre Completo",
            phone="123456789",
        )
        
        
def test_user_create_rejects_role():
    with pytest.raises(ValidationError):
        UserCreate(
            email="hola123@gmail.com",
            password="hola1234",
            full_name="Nombre Completo",
            phone="123456789",
            role = "admin"
        )