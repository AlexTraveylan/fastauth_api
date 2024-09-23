import pytest
from cryptography.fernet import Fernet
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, create_engine
from sqlmodel.pool import StaticPool

from fastauth.__main__ import app
from fastauth.database.engine import get_session


@pytest.fixture
def engine():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool)
    SQLModel.metadata.create_all(engine)

    return engine


@pytest.fixture
def session(engine):
    session = next(get_session(engine))
    yield session
    session.close()


@pytest.fixture
def key():
    return Fernet.generate_key()


@pytest.fixture
def client():
    return TestClient(app)
