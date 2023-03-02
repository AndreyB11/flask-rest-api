from db import db
from datetime import datetime


class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship(
        "ItemModel", back_populates="store", lazy="dynamic")
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
