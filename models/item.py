from db import db
from datetime import datetime


class ItemModel(db.Model):
    __tablename__ = "items"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float(precision=2), nullable=False)
    brand = db.Column(db.String, nullable=True)
    image = db.Column(db.String, nullable=True)
    store_id = db.Column(db.Integer, db.ForeignKey(
        "stores.id"), nullable=True)
    store = db.relationship(
        "StoreModel", back_populates="items")
    created_at = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow)
