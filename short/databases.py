from flask import Blueprint, request, has_request_context
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.local import LocalProxy


Engine = create_engine(
    'mysql+pymysql://root@localhost:3306/shorty',
    convert_unicode=True,
    pool_recycle=900
)

Session = sessionmaker(autocommit=False, autoflush=False, bind=Engine)
Base = declarative_base()
db = Blueprint('db', __name__)


@LocalProxy
def session():
    if not has_request_context():
        return Session()

    ctx = request._get_current_object()

    try:
        session_ = ctx._current_session
    except AttributeError:
        session_ = Session()
        ctx._current_session = session_

    return session_


@db.teardown_app_request
def session_clear(exception=None):
    ctx = request._get_current_object()

    if hasattr(ctx, '_current_session'):
        if exception is not None:
            ctx._current_session.rollback()
        ctx._current_session.close()