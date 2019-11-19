import os



class Config:
    SECRET_KEY = 'my_secret_key'
    PG_USER = 'natauser'
    PG_PASSWORD = "qwerty"
    PG_HOST = "localhost"
    PG_PORT = 5432
    DB_NAME = "test_flask"
    SQLALCHEMY_DATABASE_URI = f"postgresql://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{DB_NAME}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig:
    SECRET_KEY ='test_key'


class ProdConfig:
    SECRET_KEY='prod_key'


def run_config():
    env = os.environ.get("ENV")
    if env == 'TEST':
        return  TestConfig
    elif env == 'PROD':
        return ProdConfig
    else:
        return  Config

