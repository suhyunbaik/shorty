import pytest
from flask import request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

from config import config_by_name
from short.app import create_app

db = SQLAlchemy()


@pytest.fixture(scope='session')
def app():
    test_config = config_by_name['test']
    app = create_app(test_config)
    # ctx = app.app_context()
    # ctx.push()
    # request.addfinalizer(lambda: ctx.pop())
    # return app.test_client()
    return app


@pytest.fixture(scope='session')
def init_db():
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='session')
def session(init_db):
    db.session = sessionmaker(autocommit=False, autoflush=False, bind=init_db)
    ctx = request._get_current_object()
    ctx._current_session = db.Session()
    return ctx._current_session

    # Engine.execute('create database `test_shorty` default character set utf8')
    # engine = create_engine('mysql://root@localhost/test_shorty?charset=utf8')
    # yield engine
    # db.create_all()
    # db.drop_all()
