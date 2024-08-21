from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fast_zero.settings import Settings

settings = Settings()

# banco de dados
DB_ENGINE = settings.db_engine
DB_USER = settings.db_user
DB_PASSWORD = settings.db_password
DB_NAME = settings.db_name
DB_PORT = settings.db_port
DB_HOST = settings.db_host

# banco de dados de teste
TEST_DB_ENGINE = settings.test_db_engine
TEST_DB_USER = settings.test_db_user
TEST_DB_PASSWORD = settings.test_db_password
TEST_DB_NAME = settings.test_db_name
TEST_DB_PORT = settings.test_db_port
TEST_DB_HOST = settings.test_db_host


DATABASE_URI: str = f'{DB_ENGINE}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

TEST_DATABASE_URI: str = f'{TEST_DB_ENGINE}://{TEST_DB_USER}:{TEST_DB_PASSWORD}@{TEST_DB_HOST}:{TEST_DB_PORT}/{TEST_DB_NAME}'


engine = create_engine(DATABASE_URI)


def get_session():
    with Session(engine) as session:
        yield session


engine_test = create_engine(TEST_DATABASE_URI)


def get_session_test():
    with Session(engine_test) as session_test:
        yield session_test
