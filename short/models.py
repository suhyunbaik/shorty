from run import db
from datetime import datetime


class URLS(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(400), nullable=False, unique=True)
    short_url = db.Column(db.String(200), nullable=False, unique=True)
    created_at = db.Column(db.Datetime, default=datetime.utcnow())

