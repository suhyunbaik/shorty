from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from short.databases import Base


class URLS(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True)
    original_url = Column(String(400), nullable=False, unique=True)
    short_url = Column(String(200), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.utcnow())

