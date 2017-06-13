from flask_sqlalchemy import Model
from sqlalchemy import Column, DateTime
from datetime import datetime

class Base(Model):
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                                  onupdate=datetime.utcnow)
