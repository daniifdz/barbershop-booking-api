import os

import pytest
from alembic import command
from alembic.config import Config
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from fastapi.testclient import TestClient

from app.database import get_db
from app.main import app


@pytest.fixture(scope="session")
def engine():
    url = os.environ.get("TEST_DATABASE_URL")
    if not url:
        pytest.skip("TEST_DATABASE_URL is not set")

    with pytest.MonkeyPatch.context() as mp:
        mp.setenv("DATABASE_URL", url)
        command.upgrade(Config("alembic.ini"), "head")

    engine = create_engine(url)
    yield engine
    engine.dispose()


@pytest.fixture
def db_session(engine):
    with Session(engine) as session:
        yield session

    with engine.begin() as conn:
        conn.execute(
            text(
                "TRUNCATE users, services, barbers, barber_schedules, "
                "appointments RESTART IDENTITY CASCADE"
            )
        )
        
        
@pytest.fixture
def client(db_session):
    def override_get_db():
        yield db_session

    app.dependency_overrides[get_db] = override_get_db
    yield TestClient(app)
    app.dependency_overrides.clear()