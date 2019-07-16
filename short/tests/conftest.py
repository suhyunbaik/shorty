import pytest
from sqlalchemy.orm import sessionmaker, scoped_session
from config import config_by_name
from short.app import create_app
from short.databases import Base, Engine


@pytest.fixture(scope='session')
def app():
    config_name = config_by_name['test']
    app = create_app(config_name)
    app_context = app.app_context()
    app_context.push()
    yield app
    app_context.pop()


@pytest.fixture(scope='session')
def client(app):
    return app.test_client()


@pytest.fixture(scope='session')
def init_db():
    meta = Base.metadata
    meta.bind = Engine
    meta.create_all()
    yield Engine
    meta.drop_all()
    Engine.dispose()


@pytest.fixture(scope='session')
def session(init_db):
    Session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=init_db))
    yield Session
    Session.remove()

