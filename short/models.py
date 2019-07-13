from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class URLS(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(400), nullable=False)
    short_url = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow())

