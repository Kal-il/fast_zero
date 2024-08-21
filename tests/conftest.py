import factory
import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from fast_zero.app import app
from fast_zero.database import engine_test, get_session, get_session_test
from fast_zero.models import User, table_registry
from fast_zero.security import get_password_hash


@pytest.fixture
def client():
    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_test

        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def session():
    # engine = create_engine(TEST_DATABASE_URI)
    table_registry.metadata.create_all(engine_test)

    with Session(engine_test) as session:
        yield session
        session.rollback()

    table_registry.metadata.drop_all(engine_test)


@pytest.fixture
def user(session):
    password = 'testtest'
    user = User(
        username='Teste',
        email='teste@test.com',
        password=get_password_hash(password),
    )
    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture
def other_user(session):
    password = 'testtest'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )
    return response.json()['access_token']


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'test{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
