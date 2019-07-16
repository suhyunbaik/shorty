import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config_by_name
from short.app import create_app
from short.models import db


@pytest.fixture(scope='session')
def app():
    test_config = config_by_name['test']
    app = create_app(test_config)
    app.app_context().push()
    return app


@pytest.fixture(scope='session')
def init_db(app):
    db.init_app(app)
    db.create_all()
    yield db
    db.drop_all()


@pytest.fixture(scope='session', autouse=True)
def session(init_db):
    engine = create_engine('mysql+pymysql://root@localhost:3306/test_shorty')
    db.session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    yield db.session
    db.session.close_all()

