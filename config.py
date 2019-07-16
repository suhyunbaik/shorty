import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    set Flask configuration vars
    """
    # General config
    DEBUG = True
    TESTING = False
    # Database
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious_secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/shorty'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_HOST = 'localhost'
    SERVER_PORT = '5000'
    ENV = 'local'


class TestConfig(Config):
    """
    config for test
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/test_shorty'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    ENV = 'test'


class ProductionConfig(Config):
    """
    config for production
    """
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/shorty'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SERVER_HOST = 'localhost'
    SERVER_PORT = '5000'
    ENV = 'production'


config_by_name = dict(
    test=TestConfig,
    local=Config,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
