import pytest
from flask import request
from sqlalchemy.orm import sessionmaker

from short import databases
from sqlalchemy import create_engine

from short.app import create_app


@pytest.fixture(scope='session')
def app(request):
    config_override = {
        'TESTING': True
    }
    app = create_app(config_override)
    ctx = app.app_context()
    ctx.push()
    request.addfinalizer(lambda: ctx.pop())
    return app


@pytest.fixture(scope='session')
def init_db():
    engine = create_engine('mysql://root@localhost/test_shorty?charset=utf8')
    engine.execute('set global foreign_key_checks=0')
    databases.Base.metadata.create_all(engine)
    yield engine
    databases.Base.metadata.drop_all(engine)
    engine.dispose()


@pytest.fixture(scope='session')
def session(init_db):
    databases.Session = sessionmaker(autocommit=False, autoflush=False, bind=init_db)
    ctx = request._get_current_object()
    ctx._current_session = databases.Session()
    return ctx._current_session

