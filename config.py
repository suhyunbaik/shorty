import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    set Flask configuration vars
    """
    # General config
    DEBUG = False
    # TESTING = environ['TESTING']

    # Database
    SECRET_KEY = os.environ.get('SECRET_KEY', 'my_precious_secret_key')
    SQLALCHEMY_DATABASE_URI = 'mysql://service:uNEC8GrVBMz9RbYW@localhost:3306/shorty'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_HOST = 'localhost'
    SERVER_PORT = '5000'


class ProductionConfig(Config):
    """
    config for production
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'mysql://service:uNEC8GrVBMz9RbYW@localhost:3306/shorty'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SERVER_HOST = 'localhost'
    SERVER_PORT = '5000'


config_by_name = dict(
    local=Config,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
