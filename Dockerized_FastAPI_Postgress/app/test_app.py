from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
import pytest


from .security import manager
from .db import Base, get_db, DBContext
from .main import app

SQLALCHEMY_DATABASE_URL = "sqlite://"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)

class DBContext:

    def __init__(self):
        self.db = TestingSessionLocal()

    def __enter__(self):
        return self.db

    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()


def override_get_db():
    """override get_db"""
    with DBContext() as db:
        yield db
        
app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="module")
def client():
    with TestClient(app) as c:
      yield c

@pytest.fixture(scope="module")
def test_user():
    return {"email": "user_test@example.com","username":"user_test", "password": "pass_test"}


def test_home(client):
    """testing home page """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"Wellcome to E-Commerce Shop!"}


def test_create_user(client, test_user):
    response = client.post(
        "/users/register/",
        json = test_user)#{"email": "user_test@example.com","username":"user_test", "password": "pass_test"})
    assert response.status_code == 200, response.text
    data = response.json()
    assert data["email"] == test_user["email"]
    assert "id" in data
    user_id = data["id"]


# Notice:
#   in real project we should write more tests,
# but for time limitation in this task we write few sample test.
