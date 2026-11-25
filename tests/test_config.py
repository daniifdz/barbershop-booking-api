from app.config import get_settings


#monkeypatch: herramienta de pytest que cambia una variable de entorno solo durante ese test
#la devuelve a su estado original al terminar
def test_settings_read_database_url(monkeypatch):
    url = "postgresql+psycopg://user:pass@db:5432/testdb"
    monkeypatch.setenv("DATABASE_URL", url)
    
    assert get_settings().database_url == url