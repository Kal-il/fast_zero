from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # database
    db_engine: str
    db_host: str
    db_port: int
    db_name: str
    db_user: str
    db_password: str

    # test database
    test_db_engine: str
    test_db_host: str
    test_db_port: int
    test_db_name: str
    test_db_user: str
    test_db_password: str

    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8')
