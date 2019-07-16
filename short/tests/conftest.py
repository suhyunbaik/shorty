import pytest
from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config_by_name
from short.app import create_app
from short.databases import Base


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
def db():
    engine = create_engine(config_by_name['test'].SQLALCHEMY_DATABASE_URI, echo=True)
    session = sessionmaker(bind=engine)
    _db = {
        'engine': engine,
        'session': session
    }
    Base.metadata.create_all()
    yield _db
    Base.metadata.drop_all()
    engine.dispose()


@pytest.fixture(scope='function')
def session(db):
    session = db['session']()
    g.db = session
    yield session
    session.rollback()
    session.close()

