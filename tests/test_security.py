from app.security import hash_password, verify_password

def test_hash_is_not_the_plain_password():
    assert hash_password("hola1234") != "hola1234"
    
    
def test_verify_password_accepts_correct_password():
    hashed = hash_password("hola1234")
    assert verify_password("hola1234", hashed) == True
    
def test_verify_password_rejects_wrong_password():
    hashed = hash_password("hola1234")
    assert verify_password("dahbfa9ugfa", hashed) == False
    
def test_same_password_gives_different_hashes():
    hashed1 = hash_password("hola1234")
    hashed2 = hash_password("hola1234")
    
    assert hashed1 != hashed2
    #cada uno con su propia sal, 2 hash distintos - misma passw
    assert verify_password("hola1234", hashed1)
    assert verify_password("hola1234", hashed2)